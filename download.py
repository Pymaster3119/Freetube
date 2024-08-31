import os
import subprocess

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
