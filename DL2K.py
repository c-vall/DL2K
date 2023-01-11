from __future__ import unicode_literals
from yt_dlp import YoutubeDL
import os
from formatsettings import *

variables = {'mp3': mp3,'webm': webm}
getDir = os.getcwd()  

def logo():
    print("""\
    ____  __   ___   __  
   / __ \/ /  |__ \ / /__
  / / / / /   __/ // //_/
 / /_/ / /___/ __// ,<   
/_____/_____/____/_/|_|     
   Luffarsoft© 2023             
        """)
   
def selectVariable(name):
    return variables[name]
    
def downloadContent(link, format):
    with YoutubeDL(format) as ydl:
        ydl.download(link)

def openDirectory(format):
    if format == 'mp3':
        os.system(f'start {os.path.realpath(getDir+mp3Dir)}')
    elif format == 'webm':
        os.system(f'start {os.path.realpath(getDir+webmDir)}')
        
def main():
    while True:
        logo() 
        url = input('URL: ')
        format = input('Format: ')
        downloadContent(url, selectVariable(format))
        openDirectory(format)
        #os.system('cls')
        
if __name__ == '__main__':
    main()