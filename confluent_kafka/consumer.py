from confluent_kafka import Consumer, KafkaError

# Kafka configuration
conf = {
    'bootstrap.servers': 'localhost:9092',  # Use the IP address from your Docker Compose
    'group.id': 'my_group',  # Consumer group ID
    'auto.offset.reset': 'earliest'  # Start reading at the earliest message in the topic
}

# Create Consumer instance
consumer = Consumer(**conf)

# Subscribe to topic
topic = 'my_topic'
consumer.subscribe([topic])

# Consume messages
def consume_messages():
    try:
        while True:
            msg = consumer.poll(1.0)  # Timeout of 1 second
            
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    continue
                else:
                    # Error occurred
                    print(msg.error())
                    break
            
            # Process message
            print(f"Received message: {msg.key().decode('utf-8')}: {msg.value().decode('utf-8')}")
    except KeyboardInterrupt:
        pass
    finally:
        # Close down consumer cleanly
        consumer.close()

# Example usage
if __name__ == "__main__":
    consume_messages()
