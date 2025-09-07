import os

SIZE_OF_GET_DOCUMENTS = 100

MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
MONGO_DB = os.getenv("MONGO_DB", "tweets_db")
MONGO_URI = os.getenv("MONGO_URI", f"mongodb://{MONGO_HOST}:{MONGO_PORT}")

ELASTICSEARCH_WWW = os.getenv('ELASTICSEARCH_WWW', 'http')
ELASTICSEARCH_HOST = os.getenv('ELASTICSEARCH_HOST', 'localhost')
ELASTICSEARCH_PORT = int(os.getenv('ELASTICSEARCH_PORT', 9200))
ELASTICSEARCH_URI = os.getenv("ELASTICSEARCH_URI",f"{ELASTICSEARCH_WWW}:"
                                                  f"//{ELASTICSEARCH_HOST}:{ELASTICSEARCH_PORT}/")
ELASTICSEARCH_INDEX = os.getenv('ELASTICSEARCH_INDEX', 'meta_data_index')