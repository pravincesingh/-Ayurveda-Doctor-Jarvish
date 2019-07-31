import speech_recognition as sr
import pyttsx3
import os


speech = sr.Recognizer()

try:
    engine = pyttsx3.init()
except ImportError:
    print("Requested driver error")
except RuntimeError:
    print("Driver fails to run")

voices = engine.getProperty('voices')

engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate)

def speak(cmd):
    engine.say(cmd)
    engine.runAndWait()

def read():
    voice_text = ''
    print('Listening....')
    with sr.Microphone() as source:
        audio = speech.listen(source)
    try:
        voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print('Network error')
    return voice_text

if __name__ == '__main__':
    speak('Hello sir. How may I help You?')
    while True:
        voice_note = read()

        if 'hello' in voice_note:
            speak('Hi sir How are you?')
            continue
        elif 'open' in voice_note:
            speak('okay sir')
            os.system('explorer c:\\{}'.format(voice_note.replace('open', '')))
            continue
        elif 'bye' in voice_note:
            speak('Bye sir have a good day. thank you')
            exit()