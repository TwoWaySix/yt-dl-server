from pytube import YouTube


async def download_audio(video_id: str):
    url = f"https://www.youtube.com/watch?v={video_id}"
    yt = YouTube(url)
    return (
        yt.streams.filter(progressive=True, file_extension="mp4")
        .order_by("resolution")
        .desc()
        .first()
        .download()
    )
