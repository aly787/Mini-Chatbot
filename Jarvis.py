import speech_recognition as sr
import pyttsx3
import requests
from gtts import gTTS
import os



def speak(text):
    tts = gTTS(text=text, lang="en")
    tts.save("temp.mp3")
    os.system("mpg321 temp.mp3")  # Install mpg321 on your system to play the audio
    os.remove("temp.mp3")

def get_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en")
        print(f"User: {query}\n")
        return query
    except Exception as e:
        print(e)
        speak("Sorry, I didn't catch that. Could you please repeat?")
        return None


def get_information(query):
    # Use web scraping to get information from the web
    # For this example, let's use Wikipedia
    url = f"https://en.wikipedia.org/wiki/{query}"
    response = requests.get(url)
    if response.status_code == 200:
        speak("Here is what I found on Wikipedia.")
        # Extract and speak the first paragraph from the Wikipedia page
        # You can use BeautifulSoup or other libraries for better parsing
        info = " ".join(response.text.split("\n\n")[1].split("\n")[:3])
        print(info)
        speak(info)
    else:
        speak("Sorry, I couldn't find any information for that topic.")

def process_command(command):
    if "information about" in command:
        query = command.replace("information about", "").strip()
        get_information(query)
    else:
        speak("Sorry, I don't understand that command.")

def main():
    speak("Hello! How can I assist you today?")
    while True:
        command = get_audio().lower()
        if command:
            if "exit" in command or "bye" in command:
                speak("Goodbye!")
                break
            process_command(command)

if __name__ == "__main__":
    main()
