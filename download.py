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
    subprocess.run(["ffmpeg", "-i", "output.mov", "-q:a", "0", "-map", "a", "output.mp3", "-y"])


def download_youtube_video(url):
    try:
        os.system("rm output* -f")
        os.system(f"yt-dlp -o 'output.%(ext)s' {url}")
        command = ["yt-dlp", "--print", "filename", url]
        filename = subprocess.check_output(command, universal_newlines=True).strip()

        # Extract the file extension
        name, extension = os.path.splitext(filename)
        os.system("rm -f output.mov")
        print(extension)
        convert_to_mov("output" + extension, "output.mov")
    except:
        pass
