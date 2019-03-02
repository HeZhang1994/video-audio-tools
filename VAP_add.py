### Function: Add audio to video.

# Note: 
#     The input video should have no audio.
#     If the input video has audio, this code will not add audio.

from pathlib import Path
import os
import subprocess


# Set the name/path of input and output files.
in_video = "Media/JJY_HZY1080P.mp4"
in_audio = "Media/JJY_HZY.wav"
out_file = "Media/JJY_HZY1080P_S.mp4"

# Check if output file exists. If so, delete it.
file = Path(out_file)
if file.exists():
    os.remove(out_file)

# Process video and/or audio.
command = "ffmpeg -i " + in_video + " -i " + in_audio + " -c:v copy -c:a aac -strict experimental " + out_file

subprocess.call(command, shell=True)
