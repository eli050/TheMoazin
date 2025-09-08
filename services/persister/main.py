from elasticsearch import Elasticsearch
from config import *
from services.persister.read_wav import ReadWAV
from libs.mongo_client.connection import Connection
from libs.mongo_client.dal import MongoDAL
from libs.kafka_obj.consumer import Consumer
from libs.elasticsearch.dal import ElasticDAL
from pymongo import MongoClient
from logger import Logger


if __name__ == '__main__':
    logger = Logger.get_logger()
    try:
        conn = Connection(MongoClient(MONGO_URI),MONGO_DB)
        cons = Consumer([CONS_TOPIC_NAME])
        elastic_dal = ElasticDAL( Elasticsearch(ELASTICSEARCH_URI),ELASTICSEARCH_INDEX)
        mongo_dal = MongoDAL(conn)
        for pod in cons.consumer:
            elastic_dal.create_documents([pod.value])
            logger.info("Metadata successfully entered into Elasticsearch")
            mongo_dal.insert_binary(pod.value["file_id"],ReadWAV(pod.value["file_path"]).read())
            logger.info("The file is saved in MongoDB.")
    except Exception as e:
        logger.error("Failed to insert data into Elastic and MongoDB")
        raise e




