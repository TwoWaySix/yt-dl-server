from http.client import HTTPResponse
from fastapi import FastAPI, BackgroundTasks, Request
import uvicorn

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from ytdl.download import download_audio

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTTPResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/download/")
async def download_from_youtube(video_id: str, background_tasks: BackgroundTasks):
    print("received", video_id)
    background_tasks.add_task(download_audio, video_id)
    return {"message": "Download started in the background"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
