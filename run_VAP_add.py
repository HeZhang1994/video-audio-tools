### Function: Add audio to video.

# Note:
#     The input video should have no audio.
#     If the input video has audio, the audio will not be added.

import os
import subprocess


# Set the name/path of input and output files.
in_video = "Media/JJY_HZY1080P.mp4"
in_audio = "Media/JJY_HZY.wav"
out_file = "Media/JJY_HZY1080P_S.mp4"

# Check if the output file exists. If so, delete it.
if os.path.isfile(out_file) is True:
    os.remove(out_file)

# Process the input video and/or the input audio.
command = "ffmpeg -i " + in_video + " -i " + in_audio + " -c:v copy -c:a aac -strict experimental " + out_file

subprocess.call(command, shell=True)
