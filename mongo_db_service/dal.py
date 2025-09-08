from mongo_db_service.connection_to_db import Connection


class DALError(Exception):
    """Base class for exceptions in this module."""
    pass

class MongoDAL:
    def __init__(self, connection: Connection):
        """Initialize with a MongoDB connection."""
        self.conn = connection
        self.db_conn = self.conn.connection

    def get_documents(self,collection_name, limit=None):
        try:
            collection_conn = self.db_conn[collection_name]
            if limit is None:
                return [dict(doc) for doc in collection_conn.find({},{"_id":0})]
            return [dict(doc) for doc in collection_conn.find({},{"_id":0}).limit(limit)]
        except Exception as e:
            raise DALError(f"Error retrieving documents: {e}")
    def insert_document(self,collection_name, doc:dict):
        try:
            collection_conn = self.db_conn[collection_name]
            collection_conn.insert_one(doc)
        except Exception as e:
            raise DALError(f"Error inserting document: {e}")