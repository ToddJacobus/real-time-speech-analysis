CHUNK = 1024
CHANNELS = 2
RATE = 44100

GOOGLE_RECOGNITION_CONFIG = {
    "sampleRateHertz": integer,
    "audioChannelCount": integer,
    "enableSeparateRecognitionPerChannel": boolean,
    "languageCode": string,
    "alternativeLanguageCodes": [
      string
    ],
    "maxAlternatives": integer,
    "profanityFilter": boolean,
    "speechContexts": [
      {
        object (SpeechContext)
      }
    ],
    "enableWordTimeOffsets": boolean,
    "enableWordConfidence": boolean,
    "enableAutomaticPunctuation": boolean,
    "diarizationConfig": {
      object (SpeakerDiarizationConfig)
    },
    "metadata": {
      object (RecognitionMetadata)
    },
    "model": string,
    "useEnhanced": boolean
}

