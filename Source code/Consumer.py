import pika

# Record the start time
start_time = time.time()


# Create a connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the same queue
channel.queue_declare(queue='queue1')

# Define a callback function for handling received messages
def callback(ch, method, properties, body):
    print(f"Received message: {body}")
    print(f"Message received in {computation_time:.6f} seconds")

# Set up the consumer to use the callback function
channel.basic_consume(queue='queue1', on_message_callback=callback, auto_ack=True)

# Record the end time
end_time = time.time()


# Calculate the computation time
computation_time = end_time - start_time
#print(f"Message received in {computation_time:.6f} seconds")

# Start consuming messages
print('Waiting for messages. To exit, press CTRL+C')
channel.start_consuming()
