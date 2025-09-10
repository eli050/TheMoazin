from elasticsearch import Elasticsearch
from config import *
from services.persister.read_wav import ReadWAV
from libs.mongo_client.connection import Connection
from libs.mongo_client.dal import MongoDAL
from libs.kafka_obj.consumer import Consumer
from libs.elasticsearch.dal import ElasticDAL
from pymongo import MongoClient
from log.logger import Logger
from speach_to_text import STT

if __name__ == '__main__':
    logger = Logger.get_logger("persister\\main_logger")
    try:
        conn = Connection(MongoClient(MONGO_URI),MONGO_DB)
        cons = Consumer([CONS_TOPIC_NAME])
        elastic_dal = ElasticDAL( Elasticsearch(ELASTICSEARCH_URI),ELASTICSEARCH_INDEX)
        mongo_dal = MongoDAL(conn)
        for pod in cons.consumer:
            pod.value["text_file"] = STT(pod.value["file_path"]).read()
            elastic_dal.create_documents([pod.value])
            logger.info("Metadata successfully entered into Elasticsearch")
            mongo_dal.insert_binary(pod.value["file_id"],ReadWAV(pod.value["file_path"]).read())
            logger.info(f"The file{pod.value["file_path"]} with id {pod.value["file_id"]} "
                        f"is saved in MongoDB.")
            cons.consumer.commit()
    except Exception as e:
        logger.error("Failed to insert data into Elastic and MongoDB")
        raise e




