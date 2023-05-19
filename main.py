from http.client import HTTPResponse
from fastapi import FastAPI, BackgroundTasks, Request

import uvicorn

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

from ytdl.download import (
    DOWNLOAD_DIRECTORY,
    download_audio,
    get_all_download_names,
)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/downloads", StaticFiles(directory="downloads"), name="downloads")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTTPResponse)
def root(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "downloads": get_all_download_names()},
    )


@app.get("/download/youtube/")
async def download_from_youtube(video_id: str, background_tasks: BackgroundTasks):
    print("received", video_id)
    background_tasks.add_task(download_audio, video_id)
    return RedirectResponse(url="/")
    # return {"message": "Download started in the background"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
