import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')

engine.setProperty('rate', 190)

engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        query = None
    return query      


if __name__ == '__main__':
    speak("Hello, how are you doing?")
    audio_text = listen()
    print(audio_text)
