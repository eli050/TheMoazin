from logger import Logger

logger = Logger.get_logger()

class ReadWAV:
    def __init__(self, file_path:str):
        self.file_path = file_path

    def read(self):
        """Reading a binary file"""
        try:
            with open(self.file_path,"rb") as audio_file:
                encoded_content = audio_file.read()
            logger.info("The binary file was read successfully.")
            return encoded_content
        except FileNotFoundError as e:
            logger.error("File not found error.")
            raise FileNotFoundError(f"File not found error: {e}")

        except Exception as e:
            logger.error(f"error:{e}")
            raise Exception(e)








