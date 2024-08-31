import os
import subprocess
from moviepy.editor import VideoFileClip, concatenate_videoclips

def convert_to_mov(input_path, output_path):
    command = [
        'ffmpeg',
        '-i', input_path,
        '-c:v', 'libx264',
        '-preset', 'fast',
        '-c:a', 'aac',
        '-strict', 'experimental',
        '-threads', '8',
        '-crf', '35',
        '-movflags', 'faststart',
        output_path
    ]
    subprocess.run(command, check=True)


def download_youtube_video(url):
    try:
        os.system(f"yt-dlp -o 'output.%(ext)s' {url}")
        os.system("rm -f output.mov")
        convert_to_mov("output.mkv", "output.mov")
    except:
        pass

if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=qj_oIo_Ncas"
    download_youtube_video(video_url)