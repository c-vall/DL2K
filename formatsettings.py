#MP3
mp3 = {
    'format': 'bestaudio/best',
    'outtmpl': '/mp3/%(title)s.%(ext)s',
    'postprocessors': 
    [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
    }
#Directory
mp3Dir = "\mp3"


#WEBM
webm = {
    'format': 'best',
    'outtmpl': '/webm/%(title)s.%(ext)s',
    'postprocessors': 
    [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'webm',
    }],
    }
#Directory
webmDir = "\webm"   


#MP4
mp4 = {
    'format': 'best',
    'outtmpl': '/mp4/%(title)s.%(ext)s',
    'postprocessors': 
    [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',
    }],
    }
#Directory
mp4Dir = "\mp4"    
