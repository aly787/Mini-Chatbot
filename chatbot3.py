import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia

def jarvis(audio):
    brain = pyttsx3.init()
    voices = brain.getProperty('voices')
    brain.setProperty('voices', voices[1].id)
    brain.say(audio)
    brain.runAndWait()

def greeting():
    jarvis("Hey, I'm Jarvis. How can I be of service")

def audio_input():
    aud = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening and processing')
        aud.pause_threshold = 0.7
        audio = aud.listen(source)
        try:
            print("understanding")
            # en-eu is simply for the accent here
            # english we can also use 'en-GB' or 'en-au'
            # for UK and Australian accents
            phrase = aud.recognize_google(audio, language='en-us')
            print("you said: ", phrase)
        except Exception as exp:
            print(exp)
            print("Can you please repeat that")
            return "None"
        return phrase

def core_code():
    greeting()
    while (True):
        phrase = audio_input().lower()
        if "open medium" in phrase:
            jarvis("Opening Medium.com")
            webbrowser.open("www.medium.com")
            continue
        elif "open google" in phrase:
            jarvis("Opening Google ")
            webbrowser.open("www.google.com")
            continue
        elif "from wikipedia" in phrase:
            # to pull information from Wiki
            jarvis("Checking the wikipedia ")
            phrase = phrase.replace("wikipedia", "")
            # it will limit the summary to four lines
            result = wikipedia.summary(phrase, sentences=4)
            jarvis("As per wikipedia")
            jarvis(result)
        elif "what is your name" in phrase:
            jarvis("I am your nameless virtual assistant")
        else:
            jarvis("Sorry")

if __name__ == '__main__':
    core_code()