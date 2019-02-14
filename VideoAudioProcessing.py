## Task description:
## Extract audio from low resolution video,
## and add audio to high resolution video.
## If high resoulution video has audio, remove it.

import subprocess


## Part 1-1 Extract audio from video.

# Input video path: Videos/JuJingyi-HongZhaoYuan360P.mp4
# Output audio path: Videos/JuJingyi-HongZhaoYuan.wav

command = "ffmpeg -i Videos/JuJingyi-HongZhaoYuan360P.mp4 -ab 160k -ac 2 -ar 44100 -vn Videos/JuJingyi-HongZhaoYuan.wav"

subprocess.call(command, shell=True)


## Part 1-2 Remove audio from video.

# Input video path: Videos/JuJingyi-HongZhaoYuan1080P.mp4
# Output video path: Videos/JuJingyi-HongZhaoYuan1080P_noS.mp4

command = "ffmpeg -y -i Videos/JuJingyi-HongZhaoYuan1080P.mp4 -an -vcodec copy Videos/JuJingyi-HongZhaoYuan1080P_noS.mp4"

subprocess.call(command, shell=True)


## Part 1-3 Add audio to video.

# Input video path: Videos/JuJingyi-HongZhaoYuan1080P_noS.mp4
# Input audio path: Videos/JuJingyi-HongZhaoYuan.wav
# Output video path: Videos/JuJingyi-HongZhaoYuan1080P_S.mp4

command = "ffmpeg -i Videos/JuJingyi-HongZhaoYuan1080P_noS.mp4 -i Videos/JuJingyi-HongZhaoYuan.wav -c:v copy -c:a aac -strict experimental Videos/JuJingyi-HongZhaoYuan1080P_S.mp4"

subprocess.call(command, shell=True)


