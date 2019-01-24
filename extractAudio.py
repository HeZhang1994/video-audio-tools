import subprocess

# Input video path: a.mp4
# Output audio path: Audio/***.wav

command = "ffmpeg -i a.mp3 -ab 160k -ac 2 -ar 44100 -vn Audio/tst.wav"

subprocess.call(command, shell=True)
