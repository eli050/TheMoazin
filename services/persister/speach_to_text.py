from faster_whisper import  WhisperModel

MODEL = WhisperModel("small", device="cpu", compute_type="int8")

class STT:
    def __init__(self, file_path:str):
        self.file_path = file_path

    def read(self):
        segments, info = MODEL.transcribe(self.file_path, language="en")
        text = "\n".join([segment.text for segment in segments])
        return text
