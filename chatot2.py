import speech_recognition as sr
import pyttsx3
import openai

openai.api_key = ""

engine = pyttsx3.init("espeak")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)

recognizer = sr.Recognizer()
mic = sr.Microphone(device_index=1)

conversation = ""
user_name = "Ali"
bot_name = "Jarvis"


while True:
    with mic as source:
        print("\n Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        audio = recognizer.listen(source)
    print("no longer listening")

    try:
        user_input = recognizer.recognize_google(audio)
    except:
        continue

    prompt = user_name + ": " + user_input + "\n" + bot_name + ":"
    conversation += prompt

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= conversation,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    response_string = response["choices"][0]["text"].replace("\n", "")
    response_string = response_string.split(user_name + ":" , 1)[0].split(bot_name + ":" , 1)[0]

    conversation += response_string + "\n"
    print(response_string)

    engine.say(response_string)
    engine.runAndWait()
