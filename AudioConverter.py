### Task description: Convert audio formats.

import subprocess


# Input audio file: a.mp4
# Output audio file: b.wav
# or Output audio path: audio/b.wav

command = "ffmpeg -i a.mp3 -ab 160k -ac 2 -ar 44100 -vn b.wav"

subprocess.call(command, shell=True)

