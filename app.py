from flask import Flask
from youtube_transcript_api import YouTubeTranscriptApi
import json


app = Flask(__name__)


@app.route("/")
def hello():
    # transcript_list = YouTubeTranscriptApi.get_transcripts(["TwJX9AHdnQg"])
    # transcript_list = transcript_list[0]
    # print(transcript_list["TwJX9AHdnQg"])
    transcript = transcriptParser("TwJX9AHdnQg")
    print(transcript)
    return transcript


def transcriptParser(youtubeid):
    transcript_list = YouTubeTranscriptApi.get_transcripts([youtubeid])
    transcript_list = transcript_list[0][youtubeid]
    summarize = ""
    for i in transcript_list:
        print(i)
        summarize += i["text"]
    return summarize


if __name__ == "__main__":
    app.run(debug=True)
