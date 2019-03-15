# Function: Extract audio from video.

import os
import subprocess


# Set the path of input and output files.
INPUT_VIDEO = "Media/JJY_HZY360P.mp4"
OUTPUT_FILE = "Media/JJY_HZY.wav"

# Check if the output file exists. If so, delete it.
if os.path.isfile(OUTPUT_FILE) is True:
    os.remove(OUTPUT_FILE)

# Set the command for processing the input video/audio.
cmd = "ffmpeg -i " + INPUT_VIDEO + " -ab 160k -ac 2 -ar 44100 -vn " + OUTPUT_FILE

# Execute the (Terminal) command within Python.
subprocess.call(cmd, shell=True)
