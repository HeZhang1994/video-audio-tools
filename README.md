# Video and Audio Processing

[![image](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/HeZhang1994/video-audio-processing/blob/master/LICENSE)
[![image](https://img.shields.io/badge/python-3.7-blue.svg)]()
[![image](https://img.shields.io/badge/status-stable-brightgreen.svg)]()
[![image](https://img.shields.io/badge/build-passing-brightgreen.svg)]()

This is a **Python** implementation of processing video and audio with **FFmpeg** libraries.

Many thanks to the contributors of FFmpeg. See more information of video and audio processing on [FFmpeg](https://www.ffmpeg.org/).

## Functions

- **Extracting** the audio from a video.

- **Adding** the audio to a video that contains no audio.

- **Removing** the audio from a video that contains audio.

- **Converting** the format of audio (e.g., WAV <-> MP3).

## Dependencies

* __ffmpeg 2.8.15__

Install **FFmpeg** on **Linux** system.
```bash
$ sudo apt-get install ffmpeg
```

Install **FFmpeg** on **Mac** system.
```bash
# Install homebrew:
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# Install ffmpeg via homebrew:
$ brew install ffmpeg
```

## Usage

Specify the path/name of input and output media (`INPUT_VIDEO`, `INPUT_AUDIO`, and `OUTPUT_FILE`) in the code.

- To **extract** the audio from a video, run `run_VAP_extract.py`.

- To **add** the audio to a video, run `run_VAP_add.py`.

- To **remove** the audio from a video, run `run_VAP_remove.py`.

- To **convert** the format of audio, run `run_VAP_convert.py`.

<br>

<i>Please star this repository if you found its content useful. Thank you very much. ^_^</i>

<i>如果该程序对您有帮助，请为该程序加星支持哈，非常感谢。^_^</i>

<i>Last updated: 31/03/2019</i>
