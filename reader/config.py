import os

TOPIC_NAME = "meta_data_topic"

BOOTSTRAP_SERVER = os.getenv("BOOTSTRAP_SERVER",'localhost:9092')

FOLDER_PATH = os.getenv("FOLDER_PATH", "C:\\podcasts")

