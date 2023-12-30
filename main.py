import pyttsx3
import webbrowser
import wikipedia
import speech_recognition as sr
import datetime
import Response


r= sr.Recognizer()


para = 0

r = sr.Recognizer()





def greeting():
    print('Hello Sir How May I Help You ')
    Speak('Hello Sir How May I Help You ')

now = int(datetime.datetime.now().hour)


def time_greeting():
    if now == 23:
        Speak("Sir Its 11pm Working Hard You Should Sleep ")
        Speak('May I Help You')
    
    if now == 18 :
        Speak('Sir its 6pm')
        Speak('May I Help You')
    
    if now == 10:
        Speak("GOOD MORNING SIR HAVE A NICE DAY")
        Speak('May I Help You')                                                                                                  
    



    if now == 13:
        Speak ("Sir its Afternoon 1pm")
        Speak('May I Help You')









def Speak(command):
    too = pyttsx3.init()
    too.say(command)
    voice = too.getProperty('voices')
    too.setProperty('voice',voice[0].id)
    too.runAndWait()
while True:

    

    with sr.Microphone() as source2:
        print("Getting_Noise......")
        r.adjust_for_ambient_noise(source2,duration=1)
        print("Listening......")

        audio2 = r.listen(source2)

        myword = r.recognize_google(audio2)
        mw = myword.lower()


        print("You : " + mw)
    if 'exit' in mw :
        Speak('ok logging out')
        break 
    else:
        Speak(disko.answers(mw))
        print("TOO : "  , disko.answers(mw)) 

































## Function List

