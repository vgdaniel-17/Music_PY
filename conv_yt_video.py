import yt_dlp
import os


def descarca_playlist_fix():
    # --- AICI ESTE LINK-UL TĂU PUS DIRECT ---
    url_playlist = "https://www.youtube.com/playlist?list=PLW6HwbdnDfmnY5Z5QRECFFYZ42UYDRl02"
    # ----------------------------------------

    # Detectăm folderul unde se află scriptul în PyCharm
    folder_curent = os.path.dirname(os.path.abspath(__file__))

    # Calea către ffmpeg.exe
    cale_ffmpeg = os.path.join(folder_curent, 'ffmpeg.exe')

    # Verificare critică pentru FFmpeg
    if not os.path.exists(cale_ffmpeg):
        print("!!! EROARE CRITICĂ !!!")
        print(f"Nu am găsit fișierul ffmpeg.exe aici: {cale_ffmpeg}")
        print("Te rog trage fișierul ffmpeg.exe în PyCharm, lângă acest script.")
        return

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',

        # Opțiuni pentru a repara sunetul pe Windows
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        'postprocessor_args': [
            '-c:v', 'copy',  # Păstrează calitatea video originală
            '-c:a', 'aac',  # Transformă sunetul în AAC (ca să nu mai ai erori)
            '-b:a', '192k'
        ],

        'merge_output_format': 'mp4',
        'ffmpeg_location': folder_curent,

        # Salvează într-un folder cu numele playlist-ului
        'outtmpl': '%(playlist_title)s/%(title)s.%(ext)s',

        'ignoreerrors': True,
        'nocheckcertificate': True,
        'quiet': False,
        'no_warnings': True,
    }

    print(f"Încep descărcarea pentru playlist-ul din cod...")
    print("Voi converti sunetul automat ca să meargă pe Windows.")

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url_playlist])
        print("\n✅ Gata! Toate videoclipurile au fost descărcate și reparate.")
    except Exception as e:
        print(f"A apărut o eroare: {e}")


if __name__ == "__main__":
    descarca_playlist_fix()