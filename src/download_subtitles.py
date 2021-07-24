import os.path
import tempfile

from youtube_dl import YoutubeDL


def download_subtitles(video_id, lang):
    temp_dir = tempfile.gettempdir()
    file_name = f'{temp_dir}/{video_id}.{lang}.vtt'

    def read_file():
        with open(file_name) as file:
            return file.read()

    if os.path.isfile(file_name):
        return read_file()

    opts = {
        'subtitleslangs': [lang],
        'writesubtitles': True,
        'writeautomaticsub': True,
        'outtmpl': tempfile.gettempdir() + "/" + "%(id)s.%(ext)s",
        'skip_download': True,
        'quiet': True,
    }
    url = f'https://www.youtube.com/watch?v={video_id}'

    with YoutubeDL(opts) as ydl:
        ydl.download([url])
        return read_file() if os.path.isfile(file_name) else None