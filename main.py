import os
import os.path
import win32com.client
import speech_recognition as sr
import tkinter as tk
import datetime
import screen_brightness_control as brightness_control
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

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
    question = "Volume value?"
    speaker.Speak(question)
    print(question)
    user_input = command()
    user_input = int(user_input)
    new_volume = (0.65*user_input)-65
    try:
        # Volume value not correctly being set
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume_ = cast(interface, POINTER(IAudioEndpointVolume))
        volume_.SetMasterVolumeLevel(new_volume, None)
        print("No")
    except:
        print("There's some error")

# Shutting down


def closing(inp_x):
    if inp_x == "s":
        try:
            print("Shutting down")
            os.system("shutdown /s /t 15")
        except:
            print("There is some issue")
    elif inp_x == "r":
        try:
            print("Shutting down")
            os.system("shutdown /r")
        except:
            print("There is some error")
    else:
        try:
            print("Logging out")
            os.system("shutdown /l")
        except:
            print("There is some error")

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
            elif "shutdown" in voice_input.lower() or "restart" in voice_input.lower() or "logout" in voice_input.lower():
                if "shutdown" in voice_input.lower():
                    closing("s")
                elif "restart" in voice_input.lower():
                    closing("r")
                elif "logout" in voice_input.lower():
                    closing("l")
        pass


# Button excutetion without being called
here = assistant()
label = tk.Label(root, text="Voice Assistant")
label.pack(pady=10)
button = tk.Button(root, text="Begin", command=lambda: assistant())
button.pack(pady=20)
root.mainloop()
