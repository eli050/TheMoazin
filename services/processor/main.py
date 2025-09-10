from elasticsearch import Elasticsearch
from libs.elasticsearch.dal import ElasticDAL
from services.processor.config import *
from services.processor.classification import Classification


if __name__ == '__main__':
    elastic_dal = ElasticDAL(Elasticsearch(ELASTICSEARCH_URI), ELASTICSEARCH_INDEX)
    for doc in elastic_dal.get_documents(SIZE_OF_GET_DOCUMENTS):
        classify_doc = Classification(doc["text_file"]).classify()
        print(classify_doc)
