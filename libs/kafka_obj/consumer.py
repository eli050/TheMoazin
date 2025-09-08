from kafka import KafkaConsumer
import json
from logger import Logger

logger = Logger.get_logger()

class Consumer:
    def __init__(self, topics:list[str], bootstrap_server:str ='localhost:9092',
                 decode:str = 'utf-8' ):
        """
        Initializes the Kafka Consumer.
        """
        self.topics = topics
        self._consumer = KafkaConsumer(
            *self.topics,
            group_id='mongo-writer-group',
            value_deserializer=lambda m: json.loads(m.decode(decode)),
            bootstrap_servers= [bootstrap_server],
            auto_offset_reset='earliest'
        )
        logger.info(f"Kafka consumer subscribed to topics '{self.topics}'.")

    @property
    def consumer(self):
        return self._consumer


