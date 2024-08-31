import tkinter as tk
import download
import cv2
from PIL import Image, ImageTk
import time
import subprocess
import json
from pydub import AudioSegment
from pydub.playback import play
import threading

cap = None
video_label = None
root = tk.Tk()
video_URL = tk.StringVar(root, "")
fps = 30
multiplier = 1
paused = False
audio_segment = None
audio_thread = None
current_audio_position = 0
start_time = 0

def update_frame():
    global cap, video_label, fps, paused, multiplier, start_time, current_audio_position
    if not paused:
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(frame)
            photo = ImageTk.PhotoImage(image=image)
            video_label.config(image=photo)
            video_label.image = photo
            root.after(int(round((1000/fps)/multiplier)), update_frame)
        else:
            cap.release()
    else:
        root.after(1, update_frame)

def play_audio():
    global audio_segment, start_time, current_audio_position, multiplier
    segment = audio_segment[current_audio_position:]
    segment = segment.speedup(playback_speed=multiplier)
    play(segment)

def load_video():
    global root, video_URL
    for i in root.winfo_children():
        i.destroy()
    
    tk.Label(root, text="Download Video").pack()
    print("Downloading video from:", video_URL.get())
    download.download_youtube_video(video_URL.get())
    play_video()


def pause():
    global paused, start_time, current_audio_position, audio_thread
    paused = not paused
    if paused:
        current_audio_position += int((time.time() - start_time) * 1000 * multiplier)
        if audio_thread and audio_thread.is_alive():
            audio_thread.join()
    else:
        start_time = time.time()
        audio_thread = threading.Thread(target=play_audio)
        audio_thread.start()

def changemultiplier(mulitplierchange):
    global multiplier, paused, current_audio_position, start_time, audio_thread
    if not paused:
        current_audio_position += int((time.time() - start_time) * 1000 * multiplier)
    multiplier = mulitplierchange
    if not paused:
        start_time = time.time()
        if audio_thread and audio_thread.is_alive():
            audio_thread.join()
        audio_thread = threading.Thread(target=play_audio)
        audio_thread.start()

def play_video():
    global cap, video_label, fps, paused, multiplier, audio_segment, audio_thread, current_audio_position, start_time
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

    audio_segment = AudioSegment.from_mp3("output.mp3")
    current_audio_position = 0
    start_time = time.time()
    audio_thread = threading.Thread(target=play_audio)
    audio_thread.start()

    toolbar = tk.Frame(root)
    toolbar.pack()
    tk.Button(toolbar, text="Pause/Play", command=pause).grid(row=1, column=1)
    tk.Button(toolbar, text="0.5x", command=lambda:changemultiplier(0.5)).grid(row=0, column=0)
    tk.Button(toolbar, text="1x", command=lambda:changemultiplier(1)).grid(row=0, column=1)
    tk.Button(toolbar, text="2x", command=lambda:changemultiplier(2)).grid(row=0, column=2)

    update_frame()

tk.Entry(root, textvariable=video_URL).pack()
tk.Button(root, text="Load Video", command=load_video).pack()

root.mainloop()