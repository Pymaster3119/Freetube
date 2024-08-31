import tkinter as tk
import download
import cv2
from PIL import Image, ImageTk
import time
import subprocess
import json
cap = None
video_label = None
root = tk.Tk()
video_URL = tk.StringVar(root, "")
fps = 30
paused = True

def update_frame():
    global cap, video_label, fps, paused
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(frame)
        photo = ImageTk.PhotoImage(image=image)
        video_label.config(image=photo)
        video_label.image = photo
        root.after(int(round(1000/fps)), update_frame)
    else:
        cap.release()
        root.destroy()

def load_video():
    global root, video_URL
    for i in root.winfo_children():
        i.destroy()
    
    tk.Label(root, text="Download Video").pack()
    print("Downloading video from:", video_URL.get())
    download.download_youtube_video(video_URL.get())
    play_video()

def play_video():
    global cap, video_label, fps, paused
    print("Playing video...")
    video_label = tk.Label(root)
    video_label.pack()
    cap = cv2.VideoCapture("output.mov")

    ffprobe_cmd = [
        'ffprobe', '-v', 'error',
        '-select_streams', 'v:0',
        '-show_entries', 'stream=r_frame_rate',
        '-of', 'json', "output.mov"
    ]
    
    result = subprocess.run(ffprobe_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    video_info = json.loads(result.stdout)
    r_frame_rate = video_info['streams'][0]['r_frame_rate']
    
    num, den = map(int, r_frame_rate.split('/'))
    fps = num / den
    print(fps)
    update_frame()

tk.Entry(root, textvariable=video_URL).pack()
tk.Button(root, text="Load Video", command=load_video).pack()



root.mainloop()