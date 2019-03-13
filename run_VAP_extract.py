### Function: Extract audio from video.

import os
import subprocess


# Set the name/path of input and output files.
in_video = "Media/JJY_HZY_360P.mp4"
out_file = "Media/JJY_HZY.wav"

# Check if the output file exists. If so, delete it.
if os.path.isfile(out_file) is True:
    os.remove(out_file)

# Process the input video and/or the input audio.
command = "ffmpeg -i " + in_video + " -ab 160k -ac 2 -ar 44100 -vn " + out_file

subprocess.call(command, shell=True)  # Run terminal command.
