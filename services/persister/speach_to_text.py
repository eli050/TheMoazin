import speech_recognition as sr
from speech_recognition import UnknownValueError
from logger import Logger
from faster_whisper import WhisperModel

logger = Logger.get_logger(name="STT_logger")

RECOGNIZER = sr.Recognizer()
MODEL = WhisperModel("tiny.en", device="cpu", compute_type="int8")

class STT:
    def __init__(self, file_path:str):
        self.file_path = file_path


    def read(self, stage:str = "offline"):
        """
        Read text from wav file uses STT.
        Works both offline and online,
        online uses Google servers,
        offline downloads local model.

        """
        stages = ["offline","online"]
        if stage not in stages:
            raise Exception(f"{stage} value error")
        else:
            if stage == "online":
                try:
                    with sr.AudioFile(self.file_path) as audio_file:
                        audio = RECOGNIZER.record(audio_file)
                        text = RECOGNIZER.recognize_google(audio, language="en-US")
                        logger.info(f"{self.file_path} STT successfully")
                        return text
                except UnknownValueError:
                    logger.debug(f"In {self.file_path} file have a sound"
                                 f" that the system doesn't know how to STT")
                except Exception as e:
                    raise e
            elif stage == "offline":
                try:
                    segments, info = MODEL.transcribe(self.file_path, language="en")
                    return "\n".join([segment.text for segment in segments])
                except Exception as e:
                    raise e

