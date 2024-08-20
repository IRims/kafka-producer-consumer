import confluent_kafka 
import json

# Kafka configuration
conf = {
    'bootstrap.servers': 'localhost:9092',  # Use the IP address from your Docker Compose
}

# Create Producer instance
producer = confluent_kafka.Producer(**conf)

# Delivery callback
def delivery_callback(err, msg):
    if err:
        print(f"Message failed delivery: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")

# Produce messages
def produce_messages(topic, messages):
    for message in messages:
        # Send message
        producer.produce(topic, key=str(message['key']), value=json.dumps(message['value']), callback=delivery_callback)
        producer.poll(0)  # Trigger delivery report callback
    
    producer.flush()  # Wait for all messages to be delivered

# Example usage
if __name__ == "__main__":
    topic = 'my_topic'
    messages = [
        {'key': 'key1', 'value': {'data': 'message 1'}},
        {'key': 'key2', 'value': {'data': 'message 2'}},
        {'key': 'key3', 'value': {'data': 'message 3'}},
    ]
    produce_messages(topic, messages)
