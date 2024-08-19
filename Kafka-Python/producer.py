from kafka import KafkaProducer
import json
from data import get_registered_users
import time


def json_serializer(data):
    return json.dumps(data).encode("utf-8")

# if we have 2 partation and 1 broker 

# producer will select the partation of its choice 
# def get_partition(key , all , available):
#     return 0

# producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
#                          value_serializer=json_serializer,
#                          partitioner=get_partition)


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=json_serializer)




if __name__ == "__main__":
    while 1==1:
        registered_user = get_registered_users()
        print(registered_user)
        producer.send("registered_user",registered_user)
        time.sleep(4)
