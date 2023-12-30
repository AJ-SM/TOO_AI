import speech_recognition as sr
import pyttsx3
#import auto
import os
import pyttsx3
import webbrowser
import wikipedia
import speech_recognition as sr
import datetime
import pyautogui
from pytube import YouTube
from PIL import Image
from pytesseract import pytesseract


import time




def answers(mw):
    if 'time' in mw :
        now = int(datetime.datetime.now().hour)
        return now
    if 'wikipedia' in mw:
        
        mw = mw.replace('wikipedia', '')
        result = wikipedia.summary(mw,sentences=5)
        print(result)
        return "According to wikipedia" +result
    if 'hello' in mw :
        return 'hello dear how are you'
         
    if 'fine' in mw:
        return 'Great'
    if 'name'in mw:
        return 'I am 2 an voice assistant'
    if 'favourite' in mw:
        dir = "C:\\Users\\anujs\\OneDrive\\Desktop\\TOO\\fav"
        songs = os.listdir(dir)
        print(songs)
        os.startfile(os.path.join(dir,songs[0]))
        return 'Playing'
    if 'download' in mw :
        import time
# i don't know what is this ?????? 
    time.sleep(5)
    im1 = pyautogui.screenshot(region=(355,60,980,35))
    im1.save(r"\Video_Download\sc.png")
    tess_p = r'\Tesseract-OCR\tesseract.exe'
    img_p = r"\Video_Download\sc.png"
    img = Image.open(img_p)
    pytesseract.tesseract_cmd = tess_p
    text = pytesseract.image_to_string(img)
    link = text[:-1]
    links = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    yl = YouTube(links)
    videos = yl.streams.get_by_itag(135)
    videos.download(r'\Video_Download')
    videos.download()
    print('Done')
    return 'downloaded'



    

      

