# Video and Audio Processing

This is the **Python** implementation of video and audio processing by using **ffmpeg**.

Functions:

1. Extact audio from video.

2. Add audio to video which has no original audio.

3. Remove audio from video.

# Environment

This code has been tested on **Ubuntu 14.04** and **MacOS High Sierra 10.13.6**.

# Language

* __Python 3.5 (3.0+)__

# Dependency

* __ffmpeg__

Command to install **ffmpeg** on **Ubuntu**:
```bash
$ sudo apt-get install ffmpeg
```

Commands to install **ffmpeg** on **MacOS**:
```bash
# Install homebrew:
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
```bash
# Install ffmpeg via homebrew:
$ brew install ffmpeg
```

# Running

For Python implemented code, run:
```bash
$ python VideoAudioProcessing.py
$ # or
$ python3 VideoAudioProcessing.py
$ # if both py2 and py3 exist on your operating system.
```

# Motivation

Only low resolution videos that downloaded from Youtube have audio. Add the related audio to high resolution videos leads to better watching experience.

