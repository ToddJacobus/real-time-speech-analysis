from handlers.audio_input_reader import AudioInputReader
from handlers.audio_processor import AudioProcessor

if __name__ == "__main__":
    reader = AudioInputReader()
    processor = AudioProcessor()

    reader.start()
    processor.start()

    print("Audio stream started...")
    
    processor.join()