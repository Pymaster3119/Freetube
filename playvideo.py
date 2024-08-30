import tkinter as tk
import download
import cv2
from PIL import Image, ImageTk
import time
cap = None
video_label = None
root = tk.Tk()
video_URL = tk.StringVar(root, "")

def update_frame():
    global cap, video_label
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(frame)
        photo = ImageTk.PhotoImage(image=image)
        video_label.config(image=photo)
        video_label.image = photo
        root.after(30, update_frame)
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
    global cap, video_label
    print("Playing video...")
    video_label = tk.Label(root)
    video_label.pack()
    cap = cv2.VideoCapture("output.mov")
    if not cap.isOpened():
        print("Error: Video file could not be opened.")
    update_frame()

tk.Entry(root, textvariable=video_URL).pack()
tk.Button(root, text="Load Video", command=load_video).pack()



root.mainloop()