FROM python:3.11

RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY static ./static
COPY templates ./templates
COPY ytdl ./ytdl
COPY main.py .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"] 