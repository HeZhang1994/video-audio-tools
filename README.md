# Video and Audio Processing

This is a **Python** implementation of video and audio processing by using **ffmpeg**.

### Functions

- Extact audio from video.

- Remove audio from video.

- Add audio to video which (must?) contains no sound.

- Convert audio formats (e.g., **.m4a** <-> **.wav** <-> **.mp3**).

## Environment

This code has been tested on **Ubuntu 16.04** and **MacOS High Sierra 10.13.6** operating systems (OSs).

## Language

* __Python 3.7 (3.0+)__

## Dependency

* __ffmpeg__

For **Ubuntu** OS, execute the following command to install **ffmpeg**:
```bash
$ sudo apt-get install ffmpeg
```

For  **MacOS** OS, execute the following commands to install **ffmpeg**:
```bash
# Install homebrew:
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# Install ffmpeg via homebrew:
$ brew install ffmpeg
```

## Usage

### To process audio and video
1.1 Set the **name/path of input/output files** in ```VideoAudioProcessing.py``` (see comments for details);

1.2 Execute the following commnd on Terminal:
```bash
~$ python VideoAudioProcessing.py
# or
~$ python3 VideoAudioProcessing.py
# if both py2 and py3 exist on your operating system.
```

### To extract audio or convert audio format
2.1 Set the **name/path of input/output files** in ```AudioExtractor.py``` (see comments for details);

2.2 Execute the following command on Terminal:
```bash
~$ python AudioExtractor.py
# or
~$ python3 AudioExtractor.py
# if both py2 and py3 exist on your operating system.
```

## Motivation

Only low resolution videos that downloaded from Youtube have audio. Add the related audio to high resolution videos leads to better watching experience.

<i>Last updated: 11/02/2019</i>
