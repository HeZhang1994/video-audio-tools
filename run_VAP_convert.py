# Function: Convert audio formats.

import os
import subprocess


# Set the path of input and output files.
INPUT_AUDIO = "Media/VideoDemo.wav"
OUTPUT_FILE = "Media/VideoDemo.mp3"

# Check if the output file exists. If so, delete it.
if os.path.isfile(OUTPUT_FILE) is True:
    os.remove(OUTPUT_FILE)

# Set the command for processing the input video/audio.
cmd = "ffmpeg -i " + INPUT_AUDIO + " -ab 160k -ac 2 -ar 44100 -vn " + OUTPUT_FILE

# Execute the (Terminal) command within Python.
subprocess.call(cmd, shell=True)
