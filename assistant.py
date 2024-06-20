import tkinter as tk
from tkinter import ttk
import speech_recognition as sr


def on_button_click():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, text)
    except sr.UnknownValueError:
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, "Sorry, I couldn't understand.")
    except sr.RequestError as e:
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, f"Error fetching results from Google Speech Recognition; {e}")


root = tk.Tk()
root.title("Speech to Text App")

main_frame = ttk.Frame(root, padding=10)
main_frame.grid(row=0, column=0)

listen_button = ttk.Button(main_frame, text="Listen", command=on_button_click)
listen_button.grid(row=0, column=0, pady=5)

text_output = tk.Text(main_frame, wrap=tk.WORD, height=5, width=50)
text_output.grid(row=1, column=0, pady=5)

root.mainloop()
