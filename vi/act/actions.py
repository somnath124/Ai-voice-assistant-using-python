import os
import subprocess as sp
from audio.speech import listen, speak
from PIL import ImageGrab
from decouple import config
import  webbrowser
programs = {
    'notepad': "notepad.exe",

    'calculator': "C:\\Windows\\System32\\calc.exe",

    'word': "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE",

    'excel': "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE",

    'powerpoint': "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
}


def open_notepad():
    os.startfile(programs['notepad'])

def open_word():
    sp.Popen(programs['word'])   

def open_excel():
    sp.Popen(programs['excel'])       

def open_ppt():
    sp.Popen(programs['powerpoint']) 

def open_cmd():
    os.startfile(programs['start cmd'])  

def open_calculator():
    sp.Popen(programs['calculator'])    

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)  

def open_website():
    speak('Which website would you like to open?')
    url = listen().lower()
    webbrowser.open(url)
        

def take_screenshot():
    media_dir=config("MEDIA_DIR")
    screeshot_file=config("SCREENSHOT_FILE")
    screenshot=ImageGrab.grab()
    screenshot.save(media_dir + "/" + screeshot_file)
    print("Screenshot saved as: " + screeshot_file)       
    speak("Screenshot saved as: " + screeshot_file) 


