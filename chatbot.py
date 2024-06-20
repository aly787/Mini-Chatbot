import os
import time
import pyaudio
import playsound
from gtts import gTTS
import openai
import speech_recognition as sr

openai.api_key = ""
lang = "en"

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)

            if "Friday" in said:
                completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": said}])
                text = completion.choices[0].message["content"]
                speech = gTTS(text=text, lang=lang, slow=False, tld="com.au")
                speech.save("welcomel.mp3")
                playsound.playsound("welcomel.mp3")
            
        except Exception as e:
            print("Exception:", e)
        
    return said

while True:
    get_audio()
