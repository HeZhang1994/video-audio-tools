# Video and Audio Processing

This is the **Python** implementation of video and audio processing by using **ffmpeg** library.

### Functions:

1. Extact audio from video.

2. Remove audio from video.

3. Add audio to video which contains no sound.

4. Convert audio format (e.g., **.m4a** <-> **.wav** <-> **.mp3**).

# Environment

This code has been tested on **Ubuntu 16.04** and **MacOS High Sierra 10.13.6**.

# Language

* __Python 3.7 (3.0+)__

# Dependency

* __ffmpeg__

Execute the following command to install **ffmpeg** on **Ubuntu**:
```bash
$ sudo apt-get install ffmpeg
```

Execute the following commands to install **ffmpeg** on **MacOS**:
```bash
# Install homebrew:
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

```bash
# Install ffmpeg via homebrew:
$ brew install ffmpeg
```

# Running

1. To process audio and video, set the name/path of input files in ```VideoAudioProcessing.py``` and execute the following commnd on Terminal:
```bash
~$ python VideoAudioProcessing.py
# or
~$ python3 VideoAudioProcessing.py
# if both py2 and py3 exist on your operating system.
```

2. To extract audio or convert audio file, execute the following command on Terminal:
```bash
~$ python AudioExtractor.py
# or
~$ python3 AudioExtractor.py
# if both py2 and py3 exist on your operating system.
```

# Motivation

Only low resolution videos that downloaded from Youtube have audio. Add the related audio to high resolution videos leads to better watching experience.
