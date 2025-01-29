from flask import Flask, render_template, request, send_file
from googleapiclient.discovery import build
import pandas as pd
import os

app = Flask(__name__)

# Replace with your API Key
API_KEY = "Use_your_Google_cloud_ApiKey"

# Initialize YouTube API client
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Function to get video comments
def get_video_comments(video_id):
    comments = []
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=50
    )
    response = request.execute()
    for item in response['items']:
        snippet = item['snippet']['topLevelComment']['snippet']
        comments.append({
            'Author': snippet['authorDisplayName'],
            'Channel URL': snippet['authorChannelUrl'],
            'Comment': snippet['textDisplay'],
            'Likes': snippet['likeCount']
        })
    return comments

# Function to get channel videos
def get_channel_videos(channel_id):
    videos = []
    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        maxResults=50,
        order="date"
    )
    response = request.execute()
    for item in response['items']:
        videos.append({
            'Video Title': item['snippet']['title'],
            'Video ID': item['id']['videoId'],
            'Published At': item['snippet']['publishedAt']
        })
    return videos

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form['url']
    if "watch" in url:
        video_id = url.split("v=")[1].split("&")[0]
        comments = get_video_comments(video_id)
        file_path = "video_comments.csv"
        pd.DataFrame(comments).to_csv(file_path, index=False)
        return send_file(file_path, as_attachment=True)
    elif "channel" in url or "user" in url:
        channel_id = url.split("/channel/")[1] if "/channel/" in url else url.split("/user/")[1]
        videos = get_channel_videos(channel_id)
        file_path = "channel_videos.csv"
        pd.DataFrame(videos).to_csv(file_path, index=False)
        return send_file(file_path, as_attachment=True)
    else:
        return "Invalid YouTube URL. Please provide a video or channel URL."

if __name__ == "__main__":
    app.run(debug=True)
