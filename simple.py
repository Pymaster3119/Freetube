from moviepy.editor import VideoFileClip
from tkinter import Tk, Label
from PIL import Image, ImageTk
import cv2
def update_frame():
    global frame_number
    if frame_number < total_frames:
        frame = video.get_frame(frame_number / fps)
        frame_number += 1

        
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        image = Image.fromarray(frame)
        photo = ImageTk.PhotoImage(image=image)

        
        label.config(image=photo)
        label.image = photo

        
        root.after(int(1000 / fps), update_frame)
    else:
        
        root.destroy()


root = Tk()
root.title("MOV Video Player")


label = Label(root)
label.pack()


video_path = "/Users/aditya/Desktop/InProgress/Freetube 2.0/output.mov"
video = VideoFileClip(video_path)
fps = video.fps
total_frames = int(video.fps * video.duration)
frame_number = 0


update_frame()


root.mainloop()