from __future__ import unicode_literals
from yt_dlp import YoutubeDL
import os
from formatsettings import *

variables = {'mp3': mp3,'webm': webm, 'mp4' : mp4, 'wav' : wav}
getDir = os.getcwd()  

logo = """\
                                    ____  __   ___   __  
                                   / __ \/ /  |__ \ / /__
                                  / / / / /   __/ // //_/
                                 / /_/ / /___/ __// ,<   
                                /_____/_____/____/_/|_|     
                                   Luffarsoft© 2023         
        """
   
def selectVariable(name):
    return variables[name]
    
def downloadContent(link, format):
    with YoutubeDL(format) as ydl:
        ydl.download(link)

def openDirectory(format):
    match format:
        case 'mp3':
            os.system(f'start {os.path.realpath(getDir+mp3Dir)}')
        case 'webm':
            os.system(f'start {os.path.realpath(getDir+webmDir)}')
        case 'mp4':
            os.system(f'start {os.path.realpath(getDir+mp4Dir)}')
        case 'wav':
            os.system(f'start {os.path.realpath(getDir+wavDir)}')

def main():
    while True:
        os.system('color 0B')
        print(logo)
        url = input('URL► ')
        format = input('Format► ')
        downloadContent(url, selectVariable(format))
        openDirectory(format)
        
if __name__ == '__main__':
    main()