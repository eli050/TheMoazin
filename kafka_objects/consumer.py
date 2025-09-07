from kafka import KafkaConsumer
import json


class Consumer:
    def __init__(self, topics:list[str], bootstrap_servers:str|list ='localhost:9092',
                 decode:str = 'utf-8' ):
        """
        Initializes the Kafka Consumer.
        """
        self.topics = topics
        self._consumer = KafkaConsumer(
            *self.topics,
            group_id='mongo-writer-group',
            value_deserializer=lambda m: json.loads(m.decode(decode)),
            bootstrap_servers= list(bootstrap_servers),
            auto_offset_reset='earliest'
        )
        print(f"Kafka consumer subscribed to topic '{self.topics}'.")

    @property
    def consumer(self):
        return self._consumer


