import moviepy.editor as moviepy
import os
import subprocess
def download_youtube_video(url):
    try:
        os.system("pip3 install yt-dlp")
        os.system(f"yt-dlp -o 'output.%(ext)s' {url}")

        video_clip = moviepy.VideoFileClip("output.mkv")
        video_clip.write_videofile("output.mov", codec="libx264", audio_codec="aac")
        video_clip.close()
    except:
        pass

if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=qj_oIo_Ncas"
    download_youtube_video(video_url)