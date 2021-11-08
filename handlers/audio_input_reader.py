# RESOURCES:
# for pyaudio input streaming https://stackoverflow.com/a/35390981

import time
import pyaudio
import wave

from common.handler import Handler
from handlers import audio_data_queue


class AudioInputReader(Handler):
    def __init__(self):
        Handler.__init__(self)
        self.output_queue = audio_data_queue
        self.audio = pyaudio.PyAudio()
        self.chunk = 1024
        self.format = pyaudio.paInt16
        self.channels = 2
        self.rate = 44100

        self.stream = self.audio.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.chunk,
            stream_callback=self.callback,
        )

    def callback(self, in_data, frame_count, time_info, status):
        data = in_data
        self.output_queue.put(data)

        return (data, pyaudio.paContinue)

    def run(self):
        while not self.is_terminated():
            time.sleep(1)

    def stop(self):
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()


