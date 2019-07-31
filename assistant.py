import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import cv2
from PIL import Image
import numpy as np
import os

engine = pyttsx3.init()

client = wolframalpha.Client('R9H998-R88PKEQYE9')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)
faceDetect = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('How may I help you?')


def myCommand():
    query = ''
    r = sr.Recognizer()
    print("Listening...")
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio)
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))
    return query
        

if __name__ == '__main__':

    while True:
    
        query = myCommand()

        if 'click' in query:
            speak('Hello joy')
            cam = cv2.VideoCapture(0)
            speak('Got it. enter your name and id.')
            name = input('Enter your name:')
            id = input('enter user id:')
            sampleNumber = 0
            while (True):
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = faceDetect.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    sampleNumber = sampleNumber + 1
                    cv2.imwrite("datasets/User." + str(name) + "." + str(id) + "." + str(sampleNumber) + ".jpg", gray[y:y + h, x:x + w])
                    cv2.rectangle(img, (x, y), (x + w, y + h), (34, 0, 245), 3)
                    cv2.waitKey(100)
                cv2.imshow("Face", img)
                cv2.waitKey(1)
                if (sampleNumber > 10):
                    break
            cam.release()
            cv2.destroyAllWindows()


        
        elif 'YouTube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')


        elif 'Google' in query:
            speak('okay')
            webbrowser.open('https://www.google.com/')


        elif 'Gmail' in query:
            speak('okay sir')
            webbrowser.open('https://mail.google.com/mail/u/0/?tab=rm#inbox')


        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))
            #continue

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()


            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')
                continue

        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
           
        elif 'hello' in query:
            speak('Hello Sir')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()
                                    
        elif 'play music' in query:
            music_folder = 'C:\\Users\\jervis1.0\\PycharmProjects\\jervis\\music\\music3.mp3'
            music1 = 'music1'
            music2 = 'music2'
            music3 = 'music3'
            music4 = 'music4'
            music5 = 'music5'
            music = [music1, music2, music3, music4, music5]
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)
                  
            speak('Okay, here is your music! Enjoy!')
            

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('Got it.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=4)
                    speak('Got it.')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('Next Command! Sir!')
        

