# Voice Assistant using Python

A voice-controlled assistant developed as part of the Oasis Infobyte Python Programming Internship (OIBSIP).

## Project Overview
This project uses speech recognition to understand spoken commands and text-to-speech to respond to the user.

## Features
- Voice input through a microphone
- Speech recognition using SpeechRecognition
- Spoken responses using pyttsx3
- Current date and time
- Google search using voice commands
- Graceful handling of unrecognized commands
- Continuous listening until the user exits

## Technologies Used
- Python
- SpeechRecognition
- Pyttsx3
- SoundDevice
- Webbrowser
- Datetime

## Requirements
Python 3.x and a working microphone. Install the required Python packages:

```bash
pip install SpeechRecognition pyttsx3 sounddevice
```

## How to Run
1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Install the required packages.
4. Run the program:

```bash
python main.py
```

5. Allow microphone access and speak a supported command.

## Example Commands
- Hello
- What is the time?
- What is today's date?
- Search for Python tutorials
- Exit

## Internship
- Track: Python Programming
- Organization: Oasis Infobyte
- Task: Voice Assistant

## Privacy Note
The assistant uses microphone input to recognize voice commands. Speak only when you want to interact with it and avoid sharing sensitive information.

## Author
Deepak Kumar
