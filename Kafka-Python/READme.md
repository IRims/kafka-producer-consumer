
## for python 3.12 python-kafka is giving issues 

so use command:

```bash
pip install git+https://github.com/dpkp/kafka-python.git

```
---

## for docker:

```bash
version: "3"
services:
  zookeeper:
    image: zookeeper
    restart: always
    container_name: zookeeper
    hostname: zookeeper
    ports:
      - 2181:2181
    environment :
      ZOO_MY_ID: 1

  kafka:
    image: wurstmeister/kafka
    container_name: kafka
    ports:
      - 9092:9092
    environment:
      KAFKA_ADVERTISED_HOST_NAME: 192.168.3.11
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181

  kafka_manager:
    image: hlebalbau/kafka-manager:stable
    container_name: kakfa-manager
    restart: always
    ports:
      - "9000:9000"
    depends_on:
      - zookeeper
      - kafka
    environment:
      ZK_HOSTS: "zookeeper:2181"
      APPLICATION_SECRET: "random-secret"
      command: -Dpidfile.path=/dev/null

```

change the IPaddress ``` KAFKA_ADVERTISED_HOST_NAME: 192.168.3.111 ``` with your ipaddress

---
## making a topic usnig Kafka manager 
go to localhost:9000  

### make a cluster
Give :
- name : YourCluserName
- host : zookeeper:2181
- enable JMX polling 
- enable active offset 
- save  
cluster created!

---

## Make a topic
Give :

name : registered_user
partation : 1
replication_factor: 1 

