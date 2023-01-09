from __future__ import unicode_literals
from yt_dlp import YoutubeDL
import os
import subprocess

#intällningar för mp3
mp3 = {
    'format': 'bestaudio/best',
    'outtmpl': '/mp3/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}

#inställningar för webm 
webm = {
    'format': 'best',
    'outtmpl': '/webm/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'webm',
    }],
}

variables = {
    'mp3': mp3,
    'webm': webm
}

getDir = os.getcwd()  
mp3Dir = "\mp3"
webmDir = "\webm"

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
        os.system('cls')
        
if __name__ == '__main__':
    main()