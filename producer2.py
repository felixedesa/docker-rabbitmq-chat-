import pika
import sys

# RabbitMQ connection parameters
credentials = pika.PlainCredentials("guest", "guest")
conn_params = pika.ConnectionParameters("localhost", credentials=credentials)
conn_broker = pika.BlockingConnection(conn_params)
channel = conn_broker.channel()

# Declare exchange
channel.exchange_declare(
    exchange="chat-exchange",
    exchange_type="direct",
    durable=True
)

def send_message():
    print("Enter 'quit' to exit the chat.")
    while True:
        # Input recipient and message
        recipient = input("Send to (username): ").strip()
        if recipient.lower() == "quit":
            print("Exiting chat...")
            break

        message = input("Message: ").strip()
        if not message:
            print("Message cannot be empty!")
            continue

        # Message properties
        msg_props = pika.BasicProperties(content_type="text/plain")

        # Publish the message to the recipient's queue
        channel.basic_publish(
            exchange="chat-exchange",
            routing_key=recipient,  # Routing key is the recipient's username
            body=message,
            properties=msg_props
        )
        print(f"Sent to {recipient}: {message}")

# Start sending messages
try:
    send_message()
finally:
    conn_broker.close()
