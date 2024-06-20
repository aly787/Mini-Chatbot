from gtts import gTTS
import os
import pyttsx3
import speech_recognition as sr
import openai

# Initialize the speech recognition engine
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

# Initialize the OpenAI API
openai.api_key = ""

def respond(text):
    # Generate a response from ChatGPT
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=text,
        temperature=1,
        max_tokens=256
    )
    return response.choices[0].text.strip()

def main():
    # Start listening for user input
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # Recognize the user's speech
    try:
        user_input = recognizer.recognize_google(audio)
        print("You said:", user_input)
    except sr.UnknownValueError:
        print("I didn't understand that.")
        return

    # Respond to the user's query
    response = respond(user_input)
    print("Assistant:", response)

    # Text-to-Speech using gTTS
    tts = gTTS(text=response, lang='en')
    tts.save("response.mp3")
    os.system("afplay response.mp3")  # On macOS, plays the generated response.mp3 using afplay
    # You can use different commands based on your OS to play the generated response.mp3
    # For example, on Windows, you could use 'start response.mp3'

    # Remove the generated response.mp3 file
    os.remove("response.mp3")

if __name__ == "__main__":
    main()
