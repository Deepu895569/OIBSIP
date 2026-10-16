
import sounddevice as sd
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
from urllib.parse import quote_plus

# ---------------- CONFIGURATION ----------------

SAMPLE_RATE = 16000
DURATION = 7
MICROPHONE_DEVICE = 1

# Initialize voice engine and recognizer
engine = pyttsx3.init()
recognizer = sr.Recognizer()

recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True


# ---------------- SPEAK FUNCTION ----------------

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


# ---------------- LISTEN FUNCTION ----------------

def listen():
    print("\nGet ready to speak.")
    print("Recording starts now. Speak clearly for 7 seconds!")

    try:
        audio = sd.rec(
            int(DURATION * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="int16",
            device=MICROPHONE_DEVICE
        )

        sd.wait()

        recorded_audio = sr.AudioData(
            audio.tobytes(),
            SAMPLE_RATE,
            2
        )

        print("Recognizing your voice...")

        command = recognizer.recognize_google(
            recorded_audio,
            language="en-IN"
        )

        print("You:", command)
        return command.lower().strip()

    except sr.UnknownValueError:
        print("I could not understand the recording.")
        print("Please speak louder and try again.")
        return ""

    except sr.RequestError as error:
        print("Speech recognition service error:", error)
        print("Check your internet connection.")
        return ""

    except Exception as error:
        print("Microphone or recording error:", error)
        return ""


# ---------------- COMMAND PROCESSOR ----------------

def process_command(command):

    if not command:
        return True

    # Exit command
    if "exit" in command or "stop assistant" in command:
        speak("Goodbye! Have a nice day.")
        return False

    # Greeting
    elif "hello" in command or "hi" in command:
        speak("Hello! How can I help you?")

    # Current time
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The current time is " + current_time)

    # Current date
    elif "date" in command or "today" in command:
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + current_date)

    # Help
    elif "help" in command or "what can you do" in command:
        speak(
            "I can greet you, tell you the date and time, "
            "and search Google for information. "
            "Say exit to close me."
        )

    # Google search
    elif "search" in command or "google" in command:
        speak("What would you like to search for?")
        topic = listen()

        if topic:
            url = (
                "https://www.google.com/search?q="
                + quote_plus(topic)
            )
            webbrowser.open(url)
            speak("I opened Google search results for " + topic)

    # Unknown command
    else:
        speak(
            "Sorry, I do not know that command yet. "
            "Say help to hear my available commands."
        )

    return True


# ---------------- MAIN PROGRAM ----------------

def main():
    speak("Hello! I am your Python voice assistant.")
    speak("Say hello, ask for the date or time, or say help.")
    speak("Say exit whenever you want to stop.")

    running = True

    while running:
        command = listen()
        running = process_command(command)


# ---------------- START PROGRAM ----------------

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nVoice assistant stopped.")
    finally:
        engine.stop()
