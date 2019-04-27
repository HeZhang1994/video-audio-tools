'''Add audio to video with FFmpeg (4.1.x).

Author: He Zhang @ University of Exeter
Date: 16th April 2019 (Update: 18th April 2019)
Contact: hz298@exeter.ac.uk zhangheupc@126.com

Copyright (c) 2019 He Zhang
'''

# Python 3.7

# Note:
#     The input video should contain no audio.
#     If it contains audio, new audio will not be added.

import os
import subprocess


# Set the path of input and output files.
INPUT_VIDEO = "Media/Demo_1080P.mp4"
INPUT_AUDIO = "Media/Demo.wav"
OUTPUT_FILE = "Media/Demo_1080P_S.mp4"

# Check if the output file exists. If so, delete it.
if os.path.isfile(OUTPUT_FILE) is True:
    os.remove(OUTPUT_FILE)

# Set the command for processing the input video/audio.
cmd = "ffmpeg -i " + INPUT_VIDEO + " -i " + INPUT_AUDIO + " -c:v copy -c:a aac -strict experimental " + OUTPUT_FILE

# Execute the (Terminal) command within Python.
subprocess.call(cmd, shell=True)
