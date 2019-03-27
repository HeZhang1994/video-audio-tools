# Function: Remove audio from video.

import os
import subprocess


# Set the path of input and output files.
INPUT_VIDEO = "Media/VideoDemo360P.mp4"
OUTPUT_FILE = "Media/VideoDemo360P_noS.mp4"

# Check if the output file exists. If so, delete it.
if os.path.isfile(OUTPUT_FILE) is True:
    os.remove(OUTPUT_FILE)

# Set the command for processing the input video/audio.
cmd = "ffmpeg -y -i " + INPUT_VIDEO + " -an -vcodec copy " + OUTPUT_FILE

# Execute the (Terminal) command within Python.
subprocess.call(cmd, shell=True)
