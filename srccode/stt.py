import os
import json
import subprocess as sp
from vosk import Model, KaldiRecognizer

class STT:
    def __init__(self, config):
        self.model = KaldiRecognizer(Model(config["VOSK_MODEL_PATH"]), 16000)

    def recognize(self, audioPath):
        try:
            with sp.Popen(['ffmpeg', '-loglevel', 'quiet', '-i', audioPath, '-ar', '16000', '-ac', '1', '-f', 's16le', '-'], stdout=sp.PIPE) as process:
                self.model.AcceptWaveform(process.stdout.read())
                os.remove(audioPath)
                return json.loads(self.model.FinalResult())["text"]
        except Exception as e:
            exit(e)