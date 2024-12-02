import pika
import sys

# RabbitMQ connection parameters
credentials = pika.PlainCredentials("guest", "guest")
conn_params = pika.ConnectionParameters("localhost", credentials=credentials)  # Fixed parentheses
conn_broker = pika.BlockingConnection(conn_params)
channel = conn_broker.channel()

# Declare exchange
channel.exchange_declare(
    exchange="hello-exchange",
    exchange_type="direct",  # Corrected parameter name
    passive=False,
    durable=True,
    auto_delete=False
)

# Message to be sent
msg = sys.argv[1]
msg_props = pika.BasicProperties()
msg_props.content_type = "text/plain"

# Publish the message
channel.basic_publish(
    body=msg,
    exchange="hello-exchange",
    properties=msg_props,  # Corrected usage of msg_props
    routing_key="hola"
)

# Close the connection
conn_broker.close()
