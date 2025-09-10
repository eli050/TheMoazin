from log.logger import Logger
from faster_whisper import WhisperModel

logger = Logger.get_logger(name="STT_logger")


MODEL = WhisperModel("tiny.en", device="cpu", compute_type="int8")

class STT:
    def __init__(self, file_path:str):
        self.file_path = file_path


    def read(self):
        """
        Read text from wav file uses STT.
        uses downloads local model.

        """
        try:
            segments, info = MODEL.transcribe(self.file_path, language="en")
            return "\n".join([segment.text for segment in segments])
        except Exception as e:
            raise e

