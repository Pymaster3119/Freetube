import cv2
from tkinter import Tk, Label
from PIL import Image, ImageTk
import time

# Function to update video frames
def update_frame():
    ret, frame = cap.read()
    if ret:
        # Convert frame to PIL Image
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(frame)
        photo = ImageTk.PhotoImage(image=image)

        # Update label with new image
        label.config(image=photo)
        label.image = photo

        # Schedule next frame update
        root.after(30, update_frame)
    else:
        # Release resources and close window if video ends
        cap.release()
        root.destroy()

# Create the main window
root = Tk()
root.title("MOV Video Player")

# Create a label to hold video frames
label = Label(root)
label.pack()

# Open video file
video_path = "/Users/aditya/Desktop/InProgress/Freetube 2.0/output.mov"
cap = cv2.VideoCapture(video_path, cv2.CAP_FFMPEG)

# Start updating frames
update_frame()

# Run the Tkinter event loop
root.mainloop()