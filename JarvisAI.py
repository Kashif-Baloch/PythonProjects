from vosk import Model, KaldiRecognizer
import pyaudio
import pyttsx3
import wikipedia
import pyjokes
import os
import webbrowser
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

#print(voices[1].id)

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

model = Model("vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()


def Listen():
    print("")
    print("Listening...")
    print("")

    while True:

        data = stream.read(4096)

        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()
            p = text[14:-3]
            print(f"You said : {p}\n")

            if len(p)>0:
                return p



while True:
    Listen()
"""
if __name__ == "__main__":
    while True:
        if 'wikipedia' in p:
            speak('Searching Wikipedia...')
            p = p.replace("wikipedia", "")
            results = wikipedia.summary(p, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open google' in p:
            webbrowser.open("google.com")

        elif 'open youtube' in p:
            webbrowser.open("youtube.com")

        elif 'open youtube' in p:
            webbrowser.open("youtube.com")

        elif 'play music' in p:
            music_dir = "E:\\New folder (6)"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif 'the time' in p:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open chrome' in p:
            chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)

        if 'how are you' in p:
            speak("what do you think")

        if 'you are fine' in p:
            speak("yes, you are right. I am fine")

        elif 'open 1920' in p:
            songpath = ("E:\\New fo\\1920 Evil Returns Apnaa Mujhe Tu Lagaa(DJKANG.Com).mp4")
            os.startfile(songpath)

        elif 'are you single' in p:
            speak("No I am in a relationship with wifi")
        
        elif 'joke' in p:
            speak(pyjokes.get_joke())

        if 'go to sleep' in p:
            speak("Ok Kashif I am going to sleep")
            exit()
            """