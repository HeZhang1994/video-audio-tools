# Video and Audio Processing

[![image](https://img.shields.io/badge/license-MIT-lightgrey.svg)]()
[![image](https://img.shields.io/badge/python-3.7-blue.svg)]()
[![image](https://img.shields.io/badge/status-stable-brightgreen.svg)]()
[![image](https://img.shields.io/badge/build-passing-brightgreen.svg)]()

This is a **Python** implementation of processing video and audio with **ffmpeg** libraries.

## Function

- Extract audio from video.

- Remove audio from video.

- Add audio to video that contains no audio.

- Convert audio formats (e.g., .wav, .mp3, etc.).

## Dependency

* __ffmpeg__

For **Linux** system, install **ffmpeg** by executing the following command in Terminal.
```bash
$ sudo apt-get install ffmpeg
```

For **Mac** system, install **ffmpeg** by executing the following commands in Terminal.
```bash
# Install homebrew:
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# Install ffmpeg via homebrew:
$ brew install ffmpeg
```

## Usage

Set the name/path of input and output media files in the code (see comments for details).

- To extract audio from video, run ```VAP_extract.py```.

- To remove audio from video, run ```VAP_remove.py```.

- To add audio to video, run ```VAP_add.py```.

- To convert audio formats, run ```VAP_convert.py```.

## Motivation

Only low resolution video that downloaded from YouTube has audio. Adding extracted audio to the corresponding high resolution video leads to better watching experience.

<br>

<i>Please star this repository if you found its content useful. Thank you very much.</i>

<i>如果该程序对您有帮助，请为该程序加星支持哈，非常感谢。</i>

<i>Last updated: 00/03/2019</i>

