import pika
import json
import sys

def on_message(ch, method, properties, body):
    # Convert message to Python dictionary
    msg_data = json.loads(body)
    sender_id = msg_data["sender_id"]
    msg = msg_data["message"]
    print(f"New message from {sender_id}: {msg}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python consumer.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]  # User's unique identifier

    try:
        # RabbitMQ connection parameters
        credentials = pika.PlainCredentials("guest", "guest")
        conn_params = pika.ConnectionParameters("rabbitmq", credentials=credentials)

        # Establish connection and channel
        with pika.BlockingConnection(conn_params) as conn_broker:
            channel = conn_broker.channel()

            # Declare exchange and queue
            channel.exchange_declare(
                exchange="chat-exchange",
                exchange_type="direct",
                passive=False,
                durable=True,
                auto_delete=False
            )

            # Create a unique queue for this user and bind it to the exchange
            queue_name = f"user-queue-{user_id}"

            # Declare the queue (durable ensures the queue survives broker restarts)
            channel.queue_declare(queue=queue_name, durable=True)

            # Bind the queue to the exchange for receiving messages for this user
            channel.queue_bind(exchange="chat-exchange", queue=queue_name, routing_key=user_id)

            print(f"Waiting for messages for user {user_id}. To exit press CTRL+C")
            channel.basic_consume(queue=queue_name, on_message_callback=on_message, auto_ack=True)

            # Start consuming messages
            channel.start_consuming()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
