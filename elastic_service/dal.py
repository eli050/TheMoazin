from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

class DAL:
    """Data Access Layer for Elasticsearch operations."""

    def __init__(self, es_client: Elasticsearch, index_name: str, mapping: dict = None):
        self.es_client = es_client
        self.index_name = index_name
        if mapping is not None:
            self.mapping = mapping
        else:
            self.mapping = DAL._get_mapping()
        self._create_index()

    def _create_index(self):
        """Create the Elasticsearch index if it doesn't exist."""
        if not self.es_client.indices.exists(index=self.index_name):
            self.es_client.indices.create(index=self.index_name, mappings=self.mapping)
            print(f"Index '{self.index_name}' created.")
        else:
            print(f"Index '{self.index_name}' already exists.")

    @staticmethod
    def _get_mapping():
        """Define the mapping for the Elasticsearch index."""
        return {
            "properties":{
                "file_id":{
                    "type":"keyword"
                },
                "file_path":{
                    "type":"keyword"
                },
                "file_size":{
                    "type":"float"
                },
                "create_time":{
                    "type":"float"
                },
                "file_name":{
                    "type":"keyword"
                },
                "permissions_file":{
                    "type":"float"
                }
            }
        }
    def create_documents(self, documents:dict):
        """Bulk insert documents into the Elasticsearch index."""
        actions = [
            {
                "_index": self.index_name,
                "_id": doc["file_id"],
                "_source": doc
            }
            for doc in documents
        ]
        try:
            response = bulk(self.es_client, actions, stats_only=False)
            return response
        except Exception as e:
            raise Exception(f"Error in bulk insert: {e}")

    def get_documents(self,size: int = 100):
        """Retrieve documents from the Elasticsearch index."""
        try:
            response = self.es_client.search(index=self.index_name, body={"query": {"match_all": {}}}, size=size)
            return [{"_id": hit["_id"],
                     **hit["_source"]}
                    for hit in
                    response["hits"]["hits"]]
        except Exception as e:
            raise Exception(f"Error searching documents: {e}")