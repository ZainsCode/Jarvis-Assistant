import speech_recognition as sr 
import musiclibrary
import webbrowser
import pyttsx3
import google.generativeai as genai
from dotenv import load_dotenv
import subprocess
import os

load_dotenv()  # Load environment variables from .env file

API_KEY_1 = os.getenv("Gemini_Api_key")  # Gemini API key from environment
recognize = sr.Recognizer()
engine = pyttsx3.init()  # Initialize text-to-speech engine


def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()


def aiprocess(command):
    """Send command to Gemini API and speak the response."""
    genai.configure(api_key=API_KEY_1)  

    model = genai.GenerativeModel(
        model_name="models/gemini-1.5-flash-latest",
        system_instruction="You are a helpful assistant that always gives short, concise answers (1–2 sentences)."
    )
    response = model.generate_content(command)

    print("hello")  # Debug print
    speak(response.text)


def processCommand(command):
    """Process the user's voice command."""
    if "open" in command:
        # Extract website name after 'open'
        words = command.split("open", 1)[1].strip()
        if words:
            website = words.replace(" ", "")
            url = f"https://{website}.com"
            speak(f"Opening {words}")
            print(f"Opening URL: {url}")
            webbrowser.open(url)
        else:
            speak("Please say the name of the website.")

    elif command.startswith("play"):
        # Play a song from music library
        song = command.split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)

    elif command.startswith("start"):
        # Launch specific applications
        app = command.split(" ")[1]
        if app == "notepad":
            subprocess.Popen(["notepad.exe"])
        elif app == "calculator":
            subprocess.Popen(["calc.exe"])
        elif app == "paint":
            subprocess.Popen(["mspaint.exe"])
        elif app == "settings" or "setting":
            subprocess.Popen(["calc.exe"])
        else:
            speak("Application not recognized.")

    else:
        # If command doesn't match, send to AI
        aiprocess(command)


if __name__ == "__main__":
    speak("Initializing jarvis")
    # Continuous listening for wake word 'jarvis'
    while True:
        r = sr.Recognizer()
        print("Recognizing.....")
        try:
            with sr.Microphone() as source:
                print("Listening.....")
                audio = r.listen(source, timeout=1, phrase_time_limit=2)
            word = r.recognize_google(audio)
            print(f"Detected: {word}")

            if word.lower() == "jarvis":
                speak("Yeah")
                with sr.Microphone() as source:
                    print("Jarvis Active.....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(f"Detected: {command}")
                    processCommand(command.lower())

        except Exception as e:
            print("Error {0}".format(e))
