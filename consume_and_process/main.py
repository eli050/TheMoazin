from elasticsearch import Elasticsearch
from config import *
from mongo_db_service.connection_to_db import Connection
from mongo_db_service.dal import MongoDAL
from kafka_objects.consumer import Consumer
from elastic_service.dal import ElasticDAL
from pymongo import MongoClient

conn = Connection(MongoClient(MONGO_URI),MONGO_DB)
cons = Consumer(CONS_TOPIC_NAME)
elastic_dal = ElasticDAL( Elasticsearch(ELASTICSEARCH_URI),ELASTICSEARCH_INDEX)
mongo_dal = MongoDAL(conn)
for pod in cons.consumer:
    pass
