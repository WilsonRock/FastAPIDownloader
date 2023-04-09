from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from pytube import YouTube

app = FastAPI()

class Msg(BaseModel):
    msg: str

@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}

@app.get("/download_video/{extension}")
async def download_video(video_url: str = Query(...), extension: str = None):
    try:
        # Instantiate a YouTube object with the video URL
        yt = YouTube(video_url)

        # Print video title
        title = yt.title

        # Filter streams by extension if specified
        if extension:
            streams = yt.streams.filter(progressive=True, file_extension=extension)
        else:
            streams = yt.streams.filter(progressive=True)

        # Get the first stream with the highest resolution and download it
        stream = streams.order_by('resolution').desc().first()
        file_path = stream.download()

        # Return the video title and file path as a response
        return {"title": title, "file_path": file_path}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/vulnerable")
async def vulnerable_page(query_param: str):
    return f"<h1>¡Hola, {query_param}!</h1>"

