import json
import requests
import speech_recognition as sr

from common.handler import Handler
from handlers import audio_data_queue

from settings import (
    CHUNK,
    CHANNELS,
    RATE,
    GOOGLE_RECOGNITION_CONFIG
)


class AudioProcessor(Handler):
    def __init__(self):
        Handler.__init__(self)
        self.input_queue = audio_data_queue
        self.chunk = CHUNK
        self.channels = CHANNELS
        self.rate = RATE
        self.recognitionConfig = GOOGLE_RECOGNITION_CONFIG

        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 1

    def run(self):
        while not self.is_terminated():
            rawData = self.input_queue.get()

            audioData = sr.AudioData(
                frame_data=rawData,
                sample_rate=self.rate,
                sample_width=self.channels,
            )

            try:
                # text = self.recognizer.recognize_google(
                #     audioData,
                # )

                # See: https://cloud.google.com/speech-to-text/docs/reference/rest/v1/speech/recognize#http-request
                response = requests.post('https://speech.googleapis.com/v1/speech:recognize', data={
                    "config": self.recognitionConfig,
                    "audio": rawData
                })

                print("Recognized Audio:", text)
            except sr.UnknownValueError:
                # This exception is raised if there is no recognized speach
                pass
            except sr.RequestError:
                print("Network error.  Check API connection")
                raise
            except:
                raise


            self.input_queue.task_done()

            

