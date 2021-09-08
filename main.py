from flask import Flask, render_template, request
from pytube import YouTube
from moviepy.editor import *
import shutil

app = Flask(__name__)



def download(url):
    print("Downloading . . . ")
    mp4 = url.streams.get_highest_resolution().download()
    video_clip = VideoFileClip(mp4)
    video_clip.close()
    shutil.move(mp4, "C:\\Users\Sourabh\Downloads")
    print(" Download Complete")

@app.route('/', methods= ['POST'])
def index():
    if request.method == 'POST':
        url = YouTube(request.form.get("url"))
        download(url)
    return render_template("signup.html")



if __name__ == '__main__':
    app.run()