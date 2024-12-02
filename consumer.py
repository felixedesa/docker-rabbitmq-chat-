import pika

# RabbitMQ connection parameters
credentials = pika.PlainCredentials("guest", "guest")
conn_params = pika.ConnectionParameters("localhost", credentials=credentials)

# Establish connection
conn_broker = pika.BlockingConnection(conn_params)
channel = conn_broker.channel()

# Declare exchange
channel.exchange_declare(
    exchange="hello-exchange",
    exchange_type="direct",  # Correct parameter name for exchange type
    passive=False,
    durable=True,
    auto_delete=False
)

# Declare and bind queue
channel.queue_declare(queue="hello-queue")
channel.queue_bind(queue="hello-queue", exchange="hello-exchange", routing_key="hola")

def msg_consumer(channel, method, properties, body):
    channel.basic_ack(delivery_tag=method.delivery_tag)
    
    # Decode body to string (assuming UTF-8 encoding)
    message = body.decode('utf-8')
    
    if message == "quit":
        channel.basic_cancel(consumer_tag="hello-consumer")
        channel.stop_consuming()
    else:
        print(message)

# Start consuming
channel.basic_consume(
    on_message_callback=msg_consumer,  # Correct callback parameter
    queue="hello-queue",
    consumer_tag="hello-consumer"
)

# Start the consumer loop
channel.start_consuming()
