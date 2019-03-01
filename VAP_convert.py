### Function: Convert audio formats.

from pathlib import Path
import os
import subprocess


# Set the name/path of input and output files.
in_audio = "Media/JJY_HZY.wav"
out_file = "Media/JJY_HZY.mp3"

# Check if output file exists. If so, delete it.
file = Path(out_file)
if file.exists():
    os.remove(out_file)

# Process video and/or audio.
command = "ffmpeg -i " + in_audio + " -ab 160k -ac 2 -ar 44100 -vn " + out_file

subprocess.call(command, shell=True)  # Run terminal command.

