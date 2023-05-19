from pathlib import Path
from typing import List
from pytube import YouTube
import os

DOWNLOAD_DIRECTORY: Path = Path("./downloads")


async def download_audio(video_id: str):
    url = f"https://www.youtube.com/watch?v={video_id}"
    yt = YouTube(url)
    download_path = (
        yt.streams.filter(progressive=True, file_extension="mp4")
        .order_by("resolution")
        .desc()
        .first()
        .download(DOWNLOAD_DIRECTORY)
    )
    download_path = Path(download_path)

    audio_path = download_path.parent.joinpath(f"{download_path.name}.mp3")
    # TODO: Extract Audio
    cmd = f'ffmpeg -y -i "{download_path}" -map 0:a -acodec libmp3lame "{audio_path}"'
    os.system(cmd)
    os.remove(download_path)


def get_all_download_names() -> List[str]:
    return [p.name for p in DOWNLOAD_DIRECTORY.glob("*")]
