import os
from yt_dlp import YoutubeDL
from remove_duplicates import clean_links

output_folder = r"E:\Music Py\Videos"
links_file = 'links.txt'

cleaner = clean_links(links_file)

start_index = 9 # -> index_start


cookies_file = None

os.makedirs(output_folder, exist_ok=True)

    
ydl_opts = {
    'format' : 'bestaudio/best',

    'outtmpl': os.path.join(
        output_folder,
        '%(autonumber)d - %(title)s.%(ext)s'
    ),

    'autonumber_start': start_index,

    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320', 
    }], 

    'ffmpeg_location' : r"C:\ffmpeg\ffmpeg-7.1.1-essentials_build\bin\ffmpeg.exe",
    'keepvideo': False,

    'live_form_start': True,
    'concurrent_fragment_downloads': 1,

    'ignoreerrors': True,
    'quiet': False,
    'verbose': True,
}

with open(links_file, 'r', encoding='utf-8') as f:
    links = [line.strip() for line in f if line.strip()]

with YoutubeDL(ydl_opts) as ydl:
    ydl.download(links)


print ("Gata!!!!")