import pika
import time

# Function to read the content of a file
def read_file_content(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

# Specify the path to the file you want to read
file_path = '/content/data.json'

# Number of messages to send
num_messages = 100

# Target send rate (messages per second)
target_send_rate = 75

# Calculate the delay between messages to achieve the target send rate
delay_between_messages = 1 / target_send_rate

# Create a connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue
channel.queue_declare(queue='queue1')

# Record the start time
start_time = time.time()

# Loop to send messages
for i in range(num_messages):
    # Read the content of the file
    file_content = read_file_content(file_path)

    # Publish the file content as a message to the queue
    channel.basic_publish(exchange='', routing_key='queue1', body=file_content)

    print(f"Message {i+1} published from file content")

    # Introduce a delay between messages to achieve the target send rate
    time.sleep(delay_between_messages)

# Record the end time
end_time = time.time()

# Calculate the actual send rate
actual_send_rate = num_messages / (end_time - start_time)

print(f"Target Send Rate: {target_send_rate} messages per second")
print(f"Actual Send Rate: {actual_send_rate:.2f} messages per second")

# Close the connection
connection.close()
