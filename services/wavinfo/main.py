from read_metadata import ReadMetaData
from config import *
from libs.kafka_obj.producer import Producer
from logger import Logger



if __name__ == '__main__':
    logger = Logger.get_logger()
    try:
        producer = Producer(BOOTSTRAP_SERVER)
        reader = ReadMetaData(FOLDER_PATH)
        for md_file in reader.read_folder():
            producer.publish_message(TOPIC_NAME,md_file)
            logger.info(f"publish message in Kafka in topic: {TOPIC_NAME}")
    except Exception as e:
        logger.error("Failed to send messages in Kafka")
        raise e






