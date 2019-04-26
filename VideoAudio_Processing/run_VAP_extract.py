'''Extract audio from video with FFmpeg (4.1.x).

Author: He Zhang @ University of Exeter
Date: 16th April 2019 (Update: 18th April 2019)
Contact: hz298@exeter.ac.uk zhangheupc@126.com

Copyright (c) 2019 He Zhang
'''

# Python 3.7

import os
import subprocess


# Set the path of input and output files.
INPUT_VIDEO = "Media/Demo_HZY360P.mp4"
OUTPUT_FILE = "Media/Demo_HZY.wav"

# Check if the output file exists. If so, delete it.
if os.path.isfile(OUTPUT_FILE) is True:
    os.remove(OUTPUT_FILE)

# Set the command for processing the input video/audio.
cmd = "ffmpeg -i " + INPUT_VIDEO + " -ab 160k -ac 2 -ar 44100 -vn " + OUTPUT_FILE

# Execute the (Terminal) command within Python.
subprocess.call(cmd, shell=True)
