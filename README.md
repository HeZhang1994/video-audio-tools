# Video and Audio Processing

[![image](https://img.shields.io/badge/license-MIT-lightgrey.svg)]()
[![image](https://img.shields.io/badge/python-3.7-blue.svg)]()
[![image](https://img.shields.io/badge/status-stable-brightgreen.svg)]()
[![image](https://img.shields.io/badge/build-passing-brightgreen.svg)]()

This is a **Python** implementation of processing video and audio with **FFmpeg** libraries.

Many thanks to the contributors of [FFmpeg](https://www.ffmpeg.org/).

## Functions

- **Extracting** audio from video.

- **Adding** audio to the video that contains no audio.

- **Removing** audio from the video that contains audio.

- **Converting** audio formats (e.g., WAV <-> MP3).

## Dependencies

* __ffmpeg 2.8.15__

For **Linux** system, install **FFmpeg** by executing the following command in Terminal.
```bash
$ sudo apt-get install ffmpeg
```

For **Mac** system, install **FFmpeg** by executing the following commands in Terminal.
```bash
# Install homebrew:
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# Install ffmpeg via homebrew:
$ brew install ffmpeg
```

## Usage

Set the path/name of input and output media files (`INPUT_VIDEO`, `INPUT_AUDIO`, and `OUTPUT_FILE`) in the code.

- To **extract** audio from video, run `run_VAP_extract.py`.

- To **add** audio to video, run `run_VAP_add.py`.

- To **remove** audio from video, run `run_VAP_remove.py`.

- To **convert** audio formats, run `run_VAP_convert.py`.

<br>

<i>Please star this repository if you found its content useful. Thank you very much. ^_^</i>

<i>如果该程序对您有帮助，请为该程序加星支持哈，非常感谢。^_^</i>

<i>Last updated: 18/03/2019</i>
