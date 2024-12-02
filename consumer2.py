import pika

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

# Input the current user's username
username = input("Enter your username: ").strip()
if not username:
    print("Username cannot be empty!")
    exit()

# Declare and bind queue for the user
channel.queue_declare(queue=username, durable=True)
channel.queue_bind(queue=username, exchange="chat-exchange", routing_key=username)

print(f"Listening for messages sent to {username}...")

# Message handling function
def msg_consumer(ch, method, properties, body):
    # Decode the message
    message = body.decode("utf-8")
    print(f"\n[Message]: {message}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

# Start consuming messages
try:
    channel.basic_consume(queue=username, on_message_callback=msg_consumer)
    channel.start_consuming()
except KeyboardInterrupt:
    print("\nExiting...")
finally:
    conn_broker.close()
