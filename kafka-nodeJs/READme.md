# Kafka Docker Setup

This repository contains a simple setup for running Apache Kafka and Zookeeper using Docker. This setup is ideal for development and testing purposes.

## Prerequisites

Before you begin, ensure you have Docker and Node.js installed on your machine.

- [Docker](https://www.docker.com/get-started)
- [Node.js](https://nodejs.org/)
## Getting Started

Follow these steps to get Zookeeper, Kafka, and the necessary Node.js scripts running.

### Step 1: Run Zookeeper

Zookeeper is required to manage and coordinate Kafka brokers. Use the following command to start a Zookeeper instance on port 2181:

```bash
docker run -p 2181:2181 zookeeper
```
### Step 2: Run Kafka

```bash
docker run -p 9092:9092 \
-e KAFKA_ZOOKEEPER_CONNECT=<IP-Address>:2181 \
-e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://<IP-Address>:9092 \
-e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 \
confluentinc/cp-kafka
```

replace the ```bash<IP-Address>``` with your ipaddress
### Step 3: npm i
to install dependency kafkajs
```bash
npm i

```

### Step 3: Run admin.js

```bash

node admin.js

```


### Step 4: Run producer.js

```bash

node  producer.js

```

### Step 5: Run consumer.js

```bash

node  consumer.js <group-name>

```
Replace `<group-name>` with your desired Kafka consumer group name




