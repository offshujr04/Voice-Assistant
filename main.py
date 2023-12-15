import os.path
import win32com.client
import speech_recognition as sr
import tkinter as tk
# import pyaudio

speaker = win32com.client.Dispatch("SAPI.SpVoice")
s = "Wassup"

# Creating tkinter window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False,False)
root.title("AI Voice Assistant")


# Take command through user
def command():
    print("Waiting for input...")
    mic = sr.Recognizer()
    with sr.Microphone() as source:
        print("Waiting for input...")
        mic.pause_threshold=0.5
        audio=mic.listen(source)

        try:
            query=mic.recognize_google(audio,language="en-in")
            return query
        except sr.RequestError:
            print("Request denied")
            return ""

# Run tasks by calling different functions
def assistant():
    print("What's up")
    speaker.Speak(s)
    while True:
        print("Listening...")
        voice_input = command()
        print(f"User: {voice_input}")

        if "quit".lower() in voice_input.lower():
            print("Bye")
            exit()
        else:
            pass

# Button excutetion without being called
here = assistant()
label = tk.Label(root, text="Voice Assistant")
label.pack(pady=10)
button = tk.Button(root, text="Begin", command=lambda: assistant())
button.pack(pady=20)
root.mainloop()