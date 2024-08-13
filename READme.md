1- to activate zookeeper 2181


docker run -p 2181:2181 zookeeper



2- to activate kafka  0n 9092

docker run -p 9092:9092 \
-e KAFKA_ZOOKEEPER_CONNECT=192.168.3.11:2181 \
-e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://192.168.3.11:9092 \
-e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 \
confluentinc/cp-kafka


