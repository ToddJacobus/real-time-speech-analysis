import time
import pyaudio

from common.handler import Handler
from handlers import audio_data_queue


class AudioProcessor(Handler):
    def __init__(self):
        Handler.__init__(self)
        self.input_queue = audio_data_queue
        self.audio = pyaudio.PyAudio()
        self.chunk = 1024
        self.format = pyaudio.paInt16
        self.channels = 2
        self.rate = 44100

        self.stream = self.audio.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            output=True,
            stream_callback=self.callback,
        )

    def callback(self, in_data, frame_count, time_info, status):
        data = self.input_queue.get()
        return (data, pyaudio.paContinue)

    def run(self):
        self.stream.start_stream()
        while not self.is_terminated():
            time.sleep(1)

            

