from pathlib import Path
from typing import List
from pytube import YouTube
import os
import shutil

TEMP_DIRECTORY: Path = Path("./temp")
DOWNLOAD_DIRECTORY: Path = Path("./downloads")


async def download_audio(video_id: str):
    url = f"https://www.youtube.com/watch?v={video_id}"
    yt = YouTube(url)
    temp_path = (
        yt.streams.filter(progressive=True, file_extension="mp4")
        .order_by("resolution")
        .desc()
        .first()
        .download(TEMP_DIRECTORY)
    )
    temp_path = Path(temp_path)

    audio_temp_path = TEMP_DIRECTORY.joinpath(f"{temp_path.name}.mp3")

    cmd = f'ffmpeg -y -i "{temp_path}" -map 0:a -acodec libmp3lame "{audio_temp_path}"'
    os.system(cmd)
    os.remove(temp_path)

    audio_path = DOWNLOAD_DIRECTORY.joinpath(f"{audio_temp_path.name}")
    shutil.move(audio_temp_path, audio_path)


def get_all_download_names() -> List[str]:
    return [p.name for p in DOWNLOAD_DIRECTORY.glob("*")]
