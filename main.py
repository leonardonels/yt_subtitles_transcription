from fastapi import FastAPI
from youtube_transcript_api import YouTubeTranscriptApi

app = FastAPI()

@app.get("/")
def home():
  return {"message": "YouTube Transcript API is running!"}

@app.get("/transcript/{video_id}")
def get_transcript(video_id: str):
  try:
    if '=' in video_id:
      video_id = video_id.split('=')[1]
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return {"transcript": [entry["text"] for entry in transcript]}
  except Exception as e:
    return {"error": str(e)}
