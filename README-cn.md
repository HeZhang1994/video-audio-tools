# 视频和音频剪辑

[![image](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/HeZhang1994/video-audio-editing/blob/master/LICENSE)
[![image](https://img.shields.io/badge/python-3.7-blue.svg)]()
[![image](https://img.shields.io/badge/status-stable-brightgreen.svg)]()
[![image](https://img.shields.io/badge/build-passing-brightgreen.svg)]()

基于**Python**和**FFmpeg**实现的视频和音频剪辑。

特别鸣谢FFmpeg开源软件及其贡献者。关于更多视频和音频剪辑内容，请参考[FFmpeg官网](https://www.ffmpeg.org/).

## 目录

- [功能](#功能)
- [依赖](#依赖)
  - [基于Linux的FFmpeg](#基于Linux的FFmpeg)
  - [基于Mac的FFmpeg](#基于Mac的FFmpeg)
- [使用](#使用)
  - [视频和音频处理](#video-and-audio-processing)
  - [视频和音频剪辑](#video-and-audio-editing)

## 功能

- **Extracting** the audio from a video.

- **Adding** the audio to a video that contains no audio.

- **Removing** the audio from a video that contains audio.

- **Converting** the format of audio (e.g., WAV <-> MP3).

- **[New]** **Cutting** video/audio into clips.

- **[New]** **Merging** video/audio clips.

## 依赖

* __ffmpeg 4.1.1__ for Linux

* __ffmpeg 4.1.3__ for Mac

### FFmpeg for Linux

* Installation
```bash
$ sudo apt-get install ffmpeg
```

* Upgrade (if applicable)
```bash
# The latest version of FFmpeg is 4.x.x (11th April, 2019).
$ sudo add-apt-repository ppa:jonathonf/ffmpeg-4
$ sudo apt update && sudo apt upgrade
```

### FFmpeg for Mac

* Installation
```bash
# Install homebrew.
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
# Install FFmpeg via homebrew.
$ brew install ffmpeg
```

* Upgrade (if applicable)
```bash
# Upgrade FFmpeg to the latest version via homebrew.
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

- **[New]** To **cut** video/audio into clips, run `run_VAE_Video_01Clip.py` or `run_VAE_Audio_01Clip.py`.

- **[New]** To **merge** video/audio clips, run `run_VAE_Video_02Merge.py` or `run_VAE_Audio_02Merge.py`.

<br>

<i>Please star this repository if you found its content useful. Thank you very much. ^_^</i>

<i>如果该程序对您有帮助，请为该程序加星支持哈，非常感谢。^_^</i>

<i>Last updated: 13/04/2019</i>
