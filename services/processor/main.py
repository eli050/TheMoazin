from elasticsearch import Elasticsearch
from libs.elasticsearch.dal import ElasticDAL
from services.processor.config import *
from services.processor.classification import Classification

from logger import Logger

logger = Logger.get_logger("Classification_logger")

if __name__ == '__main__':
    elastic_dal = ElasticDAL(Elasticsearch(ELASTICSEARCH_URI), ELASTICSEARCH_INDEX)
    docs = elastic_dal.get_documents(SIZE_OF_GET_DOCUMENTS)
    logger.info("The docs returned successfully from Elasticsearch.")
    count_doc = 1
    for doc in docs:
        classify_doc = Classification(doc["text_file"]).classify()
        doc["bds_percent"] = classify_doc["bds_percent"]
        doc["bds_threat_level"] = classify_doc["bds_threat_level"]
        doc["is_bds"] = classify_doc["is_bds"]
        elastic_dal.update_documents([doc])
        logger.info(f"soc{count_doc} successfully updated")
        count_doc += 1
