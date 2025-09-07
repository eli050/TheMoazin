import base64


class ReadWAV:
    def __init__(self, file_path:str):
        self.file_path = file_path

    def read(self):
        try:
            with open(self.file_path,"rb") as audio_file:
                encoded_content = base64.b64encode(audio_file.read())
            return encoded_content
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File not found error: {e}")

        except Exception as e:
            raise Exception(e)








