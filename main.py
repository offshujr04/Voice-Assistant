import os.path
import win32com.client
import speech_recognition as sr
import tkinter as tk
import datetime
import screen_brightness_control as brightness_control

speaker = win32com.client.Dispatch("SAPI.SpVoice")
s = "Wassup"

# Creating tkinter window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title("AI Voice Assistant")


# Take command through user
def command():
    print("Waiting for input...")
    mic = sr.Recognizer()
    with sr.Microphone() as source:
        print("Waiting for input...")
        mic.pause_threshold = 0.5
        audio = mic.listen(source)

        try:
            query = mic.recognize_google(audio, language="en-in")
            return "time"
        except sr.RequestError:
            print("Request denied")
            return ""

# Finding time


def time():
    current_time = datetime.datetime.now().strftime("%H : %M : %S")
    print(current_time)
    speaker.Speak(f"The current time is {current_time}")

# Changing brightness


def brightness():
    question = "Brightness level?"
    speaker.Speak(question)
    print(question)
    user_inp = command()
    user_inp = int(user_inp)
    try:
        brightness_control.set_brightness(user_inp)
        speaker.Speak(f"Brightness has been changed to {user_inp}")
        print(f"Brightness has been changed to {user_inp}")

    except:
        print("There is some error")

# Setting volume


def volume():
    pass

# Run tasks by calling different functions


def assistant():
    print("What's up")
    speaker.Speak(s)
    while True:
        print("Listening...")
        voice_input = command()
        # print(voice_input)
        print(f"User: {voice_input}")

        if "quit".lower() in voice_input.lower():
            print("Bye")
            exit()
        else:
            if "time" in voice_input.lower():
                time()
            elif "brightness" in voice_input.lower():
                brightness()
            elif "volume" in voice_input.lower():
                volume()
        pass


# Button excutetion without being called
here = assistant()
label = tk.Label(root, text="Voice Assistant")
label.pack(pady=10)
button = tk.Button(root, text="Begin", command=lambda: assistant())
button.pack(pady=20)
root.mainloop()
