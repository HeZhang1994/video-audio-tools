# Video and Audio Processing

This is the Python code for processing video and audio using ffmpeg sofrware:

1. Extact audio from video.

2. Add audio to video which has no original audio.

3. Remove audio from video.

# Environment

* __Ubuntu 14.04__

or

* __MacOS High Sierra 10.13.6__

# Language

* __Python 3.5.2__

# Dependency

* __ffmpeg__

Command to install ffmpeg on Ubuntu:
```bash
$ sudo apt-get install ffmpeg
```

Command to install ffmpeg on MacOS:

Install homebrew:
```bash
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Install ffmpeg via homebrew:
```bash
$ brew install ffmpeg
```

# Motivation

Only low resolution videos that downloaded from Youtube have audio. Add the related audio to high resolution videos leads to better watching experience.
