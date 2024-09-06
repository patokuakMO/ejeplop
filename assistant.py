import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand.")
            return None
        except sr.RequestError:
            print("Sorry, there was an error.")
            return None

if __name__ == "__main__":
    while True:
        command = listen()
        if command:
            speak("You said: " + command)