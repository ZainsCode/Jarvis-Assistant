# 🤖 Jarvis Assistant

Jarvis Assistant is a Python-based voice assistant that can open websites, play music, launch applications, and answer questions using **Google Gemini AI**. It uses speech recognition to listen for the wake word `"jarvis"` and respond with short, concise answers.

---

## ✨ Features
- 🎙 **Voice-activated** — responds to the wake word `"jarvis"`.
- 🌐 **Open websites** by name (e.g., "open YouTube").
- 🎵 **Play music** from a predefined music library.
- ⚙ **Launch applications** like Notepad, Calculator, and Paint.
- 🤖 **Ask AI anything** using Google Gemini API.
- 🔊 **Text-to-Speech** for voice responses.

---

## 🛠 Tech Stack
- **Python 3.8+**
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [google-generativeai](https://pypi.org/project/google-generativeai/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## 📂 Project Structure
**Folder Layout:**
- **`main.py`** → Main voice assistant logic  
- **`musiclibrary.py`** → Dictionary of songs and links  
- **`requirements.txt`** → Dependencies list  
- **`README.md`** → Project documentation  

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository


```
git clone https://github.com/YourUsername/Jarvis-Assistant.git
cd Jarvis-Assistant
```
### 2️⃣ Install Dependencies
```
pip install -r requirements.txt
```
### 3️⃣ Run the Project
```
python main.py
```

### 🎯Usage
1. Say "jarvis" to activate the assistant.
2. Give commands like:
* "open YouTube"
* "play despacito"
* "start notepad"
* "what is the capital of France?"

## 📌 Example Commands

| Command             | Action                                  |
|---------------------|------------------------------------------|
| `open github`       | Opens GitHub in your browser             |
| `play shapeofyou`   | Plays the song from the music library    |
| `start calculator`  | Launches Windows Calculator              |
| `who is elon musk`  | Gets a short AI-powered answer           |


## ⚠️ Important Notes

* Do not upload your .env file to GitHub — it contains your API key.
* Works best with a clear microphone and stable internet.
* This assistant is designed for Windows (application paths may differ on Mac/Linux).

## 🤝 Contributing
I'm currently the sole developer, but contributions, suggestions, and feedback are always welcome!  
Feel free to open an issue or submit a pull request.

## 🛠️ Support
If you find a bug or have a question, open an issue in the repository.  
I'll do my best to help!
