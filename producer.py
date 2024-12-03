import pika
import sys
import json

def main():
    if len(sys.argv) < 3:
        print("Usage: python producer.py <sender_id> <receiver_id> <message>")
        sys.exit(1)

    sender_id = sys.argv[1]  # Sender's unique identifier
    receiver_id = sys.argv[2]  # Receiver's unique identifier
    msg = sys.argv[3]  # Message to be sent

    try:
        # RabbitMQ connection parameters
        credentials = pika.PlainCredentials("guest", "guest")
        conn_params = pika.ConnectionParameters("rabbitmq", credentials=credentials)

        # Establish connection and channel
        with pika.BlockingConnection(conn_params) as conn_broker:
            channel = conn_broker.channel()

            # Declare exchange for chat messages
            channel.exchange_declare(
                exchange="chat-exchange",
                exchange_type="direct",
                passive=False,
                durable=True,
                auto_delete=False
            )

            # Prepare the message with sender and receiver details
            message = json.dumps({
                "sender_id": sender_id,
                "message": msg
            })

            # Publish the message to the receiver's queue via their routing key
            channel.basic_publish(
                body=message,
                exchange="chat-exchange",
                routing_key=receiver_id,  # Direct message to the receiver
                properties=pika.BasicProperties(content_type="application/json")
            )

            print(f"Message sent from {sender_id} to {receiver_id}: {msg}")

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
