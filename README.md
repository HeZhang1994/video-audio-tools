# Video and Audio Processing

[![image](https://img.shields.io/badge/license-MIT-lightgrey.svg)]()
[![image](https://img.shields.io/badge/python-3.7-blue.svg)]()

This is a **Python** implementation for extracting/adding audio from/to video and converting audio formats with **ffmpeg**.

### Functions

- Extract audio from video.

- Remove audio from video.

- Add audio to video which (must?) contains no sound.

- Convert audio formats (e.g., **.m4a** <-> **.wav** <-> **.mp3**).

## Dependency

* __ffmpeg__

For **Ubuntu** OS, execute the following command in Terminal to install **ffmpeg**.
```bash
$ sudo apt-get install ffmpeg
```

For  **MacOS** OS, execute the following commands in Terminal to install **ffmpeg**.
```bash
# Install homebrew:
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# Install ffmpeg via homebrew:
$ brew install ffmpeg
```

## Usage

### To process audio and video (extract/add audio from/to video)

1. Set the **name/path of input/output media files** in ```VideoAudioProcessing.py``` (see comments for details).

2. Execute the following command in Terminal.
```bash
~$ python VideoAudioProcessing.py
# or
~$ python3 VideoAudioProcessing.py
# if both py2 and py3 exist on your operating system.
```

### To convert audio formats

1. Set the **name/path of input/output media files** in ```AudioConverter.py``` (see comments for details).

2. Execute the following command in Terminal.
```bash
~$ python AudioConverter.py
# or
~$ python3 AudioConverter.py
# if both py2 and py3 exist on your operating system.
```

## Motivation

Only low resolution videos that downloaded from YouTube have audio. Adding audio to the related high resolution video leads to better watching experience.

<br>

<i>Please star this repository if you found its content useful. Thank you very much.</i>

<i>如果该程序对您有帮助，请为该程序加星支持哈，非常感谢。</i>

<i>Last updated: 16/02/2019</i>

