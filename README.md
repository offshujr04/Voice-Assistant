# AI Voice Assistant

A simple Python-based AI Voice Assistant with a graphical user interface (GUI) that can respond to voice commands to perform system tasks such as:

🎤 Telling the current time

💡 Changing screen brightness

🔊 Adjusting system volume

📴 Shutting down, restarting, or logging out of the system

Built using Tkinter, speech_recognition, SAPI text-to-speech, and other system-level Python packages.

# 📦 Features

✅ Voice-activated command recognition (via microphone)

✅ Text-to-speech interaction using Windows SAPI

✅ Brightness and volume control

✅ System shutdown, restart, and logout options

✅ User-friendly GUI with a "Start" button

# 🛠 Requirements

Make sure you have the following Python libraries installed:

pip install SpeechRecognition
pip install pycaw
pip install screen-brightness-control
pip install comtypes
pip install pyaudio
pip install pywin32

# 🧠 How It Works
Launches a simple GUI window using Tkinter.

On clicking the "Begin" button:

The assistant greets the user.

Listens for a voice command.

Responds to one of the following:

"Time" → Reads current time.

"Brightness" → Asks for a brightness level and applies it.

"Volume" → Asks for a volume level and sets it.

"Shutdown", "Restart", or "Logout" → Triggers system-level command.

"Quit" → Exits the assistant.

# 🚀 Getting Started
Clone the repository or copy the code.

Run the script on a Windows machine.

Click the "Begin" button in the GUI.

Speak out commands like:

"What's the time?"

"Change brightness"

"Set volume"

"Shutdown the system"

"Quit"
