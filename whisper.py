from io import BytesIO
from openai import OpenAI
from conf import APIKEY

client = OpenAI(
  api_key = APIKEY,  # this is also the default, it can be omitted
)
import speech_recognition as sr

r = sr.Recognizer()

def get_audio_from_mic():
    with sr.Microphone(sample_rate=16000) as source:
        print("なにか話してください")
        audio = r.listen(source)
        print("考え中...")
        return audio

def voice_to_text():
    audio = get_audio_from_mic()
    audio_data = BytesIO(audio.get_wav_data())
    audio_data.name = 'from_mic.wav'
    print("Before transcript")
    transcript = client.audio.transcriptions.create( model='whisper-1', file=audio_data, response_format="text")
    print("After transcript")
    return transcript
