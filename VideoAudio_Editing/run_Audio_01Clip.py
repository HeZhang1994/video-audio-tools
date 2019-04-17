'''Function (Python3): Cut audio into clips with FFmpeg (4.1.x).

Author: He Zhang @ University of Exeter
Date: April 17th 2019 (Update: April 17th 2019)
Contact: hz298@exeter.ac.uk zhangheupc@126.com

Copyright (c) 2019 He Zhang
'''

import os
import re
import shutil
import subprocess


def calc_time_diff(time1_str, time2_str):  # Not used in this code!
    '''Function: Calculate the numerical difference of two timestamps.

    This function is used to obtain the '[duration]' based on [start_time]
    and [end_time] for cutting a media with the following FFmpeg command:
    $ ffmpeg -i in.mpn -ss [start] -t [duration] out.mpn

    Parameters:
        time1_str <str> - The previous timestamp 'hh:mm:ss'.
        time2_str <str> - The latest timestamp 'hh:mm:ss'.

    Return:
        diff_str <str> - The numerical difference of two timestamps 'hh:mm:ss'.
    '''
    # Split timestamp to hh, mm, and ss.
    time1_list = re.split('[:]', time1_str)  # <list> with 3 elements (hh, mm, ss).
    time2_list = re.split('[:]', time2_str)  # <list> with 3 elements (hh, mm, ss).

    # Convert <str> to <int> for calculation (+, *).
    time1_s = int(time1_list[0]) * 3600 + int(time1_list[1]) * 60 + int(time1_list[2])
    time2_s = int(time2_list[0]) * 3600 + int(time2_list[1]) * 60 + int(time2_list[2])

    # Calculate hh, mm, and ss of timestamp difference.
    diff = time2_s - time1_s  # Total timestamp difference (seconds).
    diff_h = diff / 3600
    diff_m = (diff % 3600) / 60
    diff_s = diff % 60

    # Concatenate hh, mm, and ss of timestamp difference.
    diff_str = str(diff_h).zfill(2) + ':' + str(diff_m).zfill(2) + ':' + str(diff_s).zfill(2)

    return diff_str


# Part 1 Set the path of input and output media.

INPUT_MEDIA = 'Media/JJY_Suddenly_PhantaCity.mp3'
# Download link: https://www.youtube.com/watch?v=Y36TtbFHm0M
OUTPUT_PATH = 'Media/Clips_Audio/'
OUTPUT_NAME = 'Clip_'
OUTPUT_TYPE = '.mp3'

# Check if the output folder exists. If so, delete it and create an empty one.
if os.path.exists(OUTPUT_PATH) is True:
    shutil.rmtree(OUTPUT_PATH)
os.mkdir(OUTPUT_PATH)


# Part 2 Set the cutting points of original media.

# The start points of clips.
LIST_START = ['00:00:45', '00:02:07', '00:10:02', '00:11:17']
# The end points of clips.
LIST_END = ['00:01:29', '00:02:40', '00:10:30', '00:11:51']

# Check the start and end points of original media.
if len(LIST_START) != len(LIST_END):
    print('Error: Start points are not matched with end points.')
else:
    num_clip = len(LIST_START)


# Part 3 Cut original media with FFmpeg command.

# $ ffmpeg -i in.mpn -ss [start] -to [end] out.mpn
# Note:
#    '[start]' - The start point of original media.
#    '[start]' - The format is 'hh:mm:ss.xxx' or 'nnn', '00:01:15.000' or '75'.
#    '[end]'   - The end point of original media.
#    '[end]'   - The format is 'hh:mm:ss.xxx' or 'nnn', '00:01:25.000' or '85'.
# Note:
#     Setting '-i in.mpn' before '-ss [start]' avoids inaccurate clips.
#     Removing 'copy' re-encodes clips and avoids black screen/frames.
#     Removing 'copy' leads to high CPU load and long operating time.
for t in range(num_clip):
    tag_start = LIST_START[t] + '.000'
    tag_end = LIST_END[t] + '.000'

    # Generate the path for saving output media.
    output_file = OUTPUT_PATH + OUTPUT_NAME + str(t + 1) + OUTPUT_TYPE

    # Generate the command for processing input media.
    cmd = 'ffmpeg -i ' + INPUT_MEDIA + ' -ss ' + tag_start + ' -to ' + tag_end + ' ' + output_file

    # Execute the (Terminal) command within Python.
    subprocess.call(cmd, shell=True)
