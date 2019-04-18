# Video and Audio Processing/Editing

[![image](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/HeZhang1994/video-audio-tools/blob/master/LICENSE)
[![image](https://img.shields.io/badge/python-3.7-blue.svg)]()
[![image](https://img.shields.io/badge/status-stable-brightgreen.svg)]()
[![image](https://img.shields.io/badge/build-passing-brightgreen.svg)]()

[*English Version*](https://github.com/HeZhang1994/video-audio-tools/blob/master/README.md) | [*中文版*](https://github.com/HeZhang1994/video-audio-tools/blob/master/README-cn.md)

This is a **Python** implementation of processing/editing video and audio with **FFmpeg** libraries.

Many thanks to FFmpeg and its contributors. For more related information, please visit [FFmpeg website](https://www.ffmpeg.org/).

## Table of Contents

- [Functions](#functions)
- [Dependencies](#dependencies)
  - [Install FFmpeg for Linux](#install-ffmpeg-for-linux)
  - [Install FFmpeg for Mac](#install-ffmpeg-for-mac)
- [Usage](#usage)
  - [Video and Audio Processing](#video-and-audio-processing)
  - [Video and Audio Editing](#video-and-audio-editing)

## Functions

- **Extracting** the audio from a video.

- **Adding** the audio to a video that contains no audio.

- **Removing** the audio from a video.

- **Converting** the format of audio.

- [**New!**] **Cutting** video or audio into clips.

- [**New!**] **Merging** video or audio clips.

## Dependencies

* __ffmpeg 4.1.1__ for Linux
* __ffmpeg 4.1.3__ for Mac

### Install FFmpeg for Linux

* Installation
```bash
$ sudo apt-get install ffmpeg
```

* Upgrade (if applicable)
```bash
# The latest version of FFmpeg is 4.1.x (11th April 2019).
$ sudo add-apt-repository ppa:jonathonf/ffmpeg-4
$ sudo apt update && sudo apt upgrade
```

### Install FFmpeg for Mac

* Installation
```bash
# Install homebrew.
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
# Install FFmpeg via homebrew.
$ brew install ffmpeg
```

* Upgrade (if applicable)
```bash
# Upgrade FFmpeg via homebrew.
$ brew update && brew upgrade ffmpeg
```

## Usage

Specify the path/name of input and output media in the code (see comments).

### Video and Audio Processing

- To **extract** the audio from a video, run `run_VAP_extract.py`.

- To **add** the audio to a video, run `run_VAP_add.py`.

- To **remove** the audio from a video, run `run_VAP_remove.py`.

- To **convert** the format of audio, run `run_VAP_convert.py`.

### Video and Audio Editing

- [**New!**] To **cut** video or audio into clips, run `run_VAE_Video_01Clip.py` or `run_VAE_Audio_01Clip.py`.

- [**New!**] To **merge** video or audio clips, run `run_VAE_Video_02Merge.py` or `run_VAE_Audio_02Merge.py`.

<br>

<i>Please star this repository if you found its content useful. Thank you very much. ^_^</i>
