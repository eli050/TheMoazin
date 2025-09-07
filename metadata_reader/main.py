from read_metadata import ReadMetaData
from config import *
from kafka_objects.producer import Producer

producer = Producer(BOOTSTRAP_SERVER)
reader = ReadMetaData(FOLDER_PATH)

for md_file in reader.read_folder():
    producer.publish_message(TOPIC_NAME,md_file)




