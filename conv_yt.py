import os
from yt_dlp import YoutubeDL

# ===== SETĂRI =====
output_folder = r"E:\Music Py\Abel"
playlist_url = "https://www.youtube.com/playlist?list=PLoe_q0X1XB7W-2WWbDxA4qup5_S_DJqKR"
start_index = 12

os.makedirs(output_folder, exist_ok=True)

# ===== DOWNLOAD FĂRĂ INDEX =====
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(
        output_folder,
        '%(title)s.%(ext)s'
    ),
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
    'ffmpeg_location': r"C:\ffmpeg\ffmpeg-7.1.1-essentials_build\bin\ffmpeg.exe",
    'keepvideo': False,
    'quiet': False,
    'no_warnings': True,
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])

# ===== RENUMEROTARE CORECTĂ DE LA 12 =====
files = sorted(
    f for f in os.listdir(output_folder)
    if f.lower().endswith(".mp3")
)

for i, filename in enumerate(files, start=start_index):
    new_name = f"{i:02d} - {filename}"
    old_path = os.path.join(output_folder, filename)
    new_path = os.path.join(output_folder, new_name)

    if not os.path.exists(new_path):
        os.rename(old_path, new_path)
