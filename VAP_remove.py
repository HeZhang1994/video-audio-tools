### Function: Remove audio from video.

from pathlib import Path
import os
import subprocess


# Set the name/path of input and output files.
in_video = "Media/JJY_HZY_360P.mp4"
out_file = "Media/JJY_HZY_360P_noS.mp4"

# Check if output file exists. If so, delete it.
file = Path(out_file)
if file.exists():
    os.remove(out_file)

# Process video and/or audio.
command = "ffmpeg -y -i " + in_video + " -an -vcodec copy " + out_file

subprocess.call(command, shell=True)
