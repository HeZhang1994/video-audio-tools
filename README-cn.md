# 视频和音频处理/剪辑

[![image](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/HeZhang1994/video-audio-editing/blob/master/LICENSE)
[![image](https://img.shields.io/badge/python-3.7-blue.svg)]()
[![image](https://img.shields.io/badge/status-stable-brightgreen.svg)]()
[![image](https://img.shields.io/badge/build-passing-brightgreen.svg)]()

[*English Version*](https://github.com/HeZhang1994/video-audio-editing/blob/master/README.md) | [*中文版*](https://github.com/HeZhang1994/video-audio-editing/blob/master/README-cn.md)

基于**Python**和**FFmpeg库**实现的处理/剪辑视频和音频。

特别鸣谢FFmpeg及其贡献者。关于更多相关内容，请访问[FFmpeg网站](https://www.ffmpeg.org/)。

## 目录

- [功能](#功能)
- [依赖项](#依赖项)
  - [安装Linux版本的FFmpeg](#安装linux版本的ffmpeg)
  - [安装Mac版本的FFmpeg](#安装mac版本的ffmpeg)
- [使用方法](#使用方法)
  - [视频和音频处理](#视频和音频处理)
  - [视频和音频剪辑](#视频和音频剪辑)

## 功能

- **提取**视频中的音频。

- **添加**音频到不含音频的视频。

- **删除**视频中的音频。

- **转换**音频的格式。

- [**新!**] **剪切**视频或音频为片段。

- [**新!**] **拼接**视频或音频的片段。

## 依赖项

* __ffmpeg 4.1.1__ （针对Linux系统）
* __ffmpeg 4.1.3__ （针对Mac系统）

### 安装Linux版本的FFmpeg

* 安装
```bash
$ sudo apt-get install ffmpeg
```

* 更新（如果适用）
```bash
# FFmpeg的最新版本为4.1.x（2019年4月11日）。
$ sudo add-apt-repository ppa:jonathonf/ffmpeg-4
$ sudo apt update && sudo apt upgrade
```

### 安装Mac版本的FFmpeg

* 安装
```bash
# 安装homebrew。
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
# 通过homebrew安装FFmpeg。
$ brew install ffmpeg
```

* 更新（如果适用）
```bash
# 通过homebrew更新FFmpeg。
$ brew update && brew upgrade ffmpeg
```

## 使用方法

参考程序注释，设置输入和输出多媒体文件的文件名/路径。

### 视频和音频处理

请使用`VideoAudio_Processing/`中提供的程序。

- 运行`run_VAP_extract.py`，**提取**视频中的音频。

- 运行`run_VAP_add.py`，**添加**音频到视频。

- 运行`run_VAP_remove.py`，**删除**视频中的音频。

- 运行`run_VAP_convert.py`，**转换**音频的格式。

### 视频和音频剪辑

请使用`VideoAudio_Editing/`中提供的程序。

- [**新!**] 运行`run_VAE_Video_01Clip.py`或`run_VAE_Audio_01Clip.py`，**剪切**视频或音频为片段。

- [**新!**] 运行`run_VAE_Video_02Merge.py`或`run_VAE_Audio_02Merge.py`，**拼接**视频或音频的片段。

<br>

<i>如果您对该项目有任何问题，请报告issue，我将会尽快回复。</i>

<i>如果该项目对您有帮助，请为其加星支持哈，非常感谢。^_^</i>
