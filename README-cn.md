# 视频和音频处理/剪辑

[![image](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/HeZhang1994/video-audio-editing/blob/master/LICENSE)
[![image](https://img.shields.io/badge/python-3.7-blue.svg)]()
[![image](https://img.shields.io/badge/status-stable-brightgreen.svg)]()
[![image](https://img.shields.io/badge/build-passing-brightgreen.svg)]()

[*English Version*](https://github.com/HeZhang1994/video-audio-editing/blob/master/README.md) | [*中文版*](https://github.com/HeZhang1994/video-audio-editing/blob/master/README-cn.md)

基于**Python**和**FFmpeg库**实现的视频和音频处理/剪辑。

特别鸣谢FFmpeg开源库及其贡献者。关于更多内容，请访问[FFmpeg官网](https://www.ffmpeg.org/).

## 目录

- [功能](#功能)
- [依赖](#依赖)
  - [安装基于Linux的FFmpeg](#安装基于linux的ffmpeg)
  - [安装基于Mac的FFmpeg](#安装基于mac的ffmpeg)
- [使用](#使用)
  - [视频和音频处理](#video-and-audio-processing)
  - [视频和音频剪辑](#video-and-audio-editing)

## 功能

- **提取**视频中的音频。

- **添加**音频到不含音频的视频。

- **删除**视频中的音频。

- **转换**音频的格式。

- **【新】** **剪切**视频或音频为片段。

- **【新】** **拼接**视频或音频的片段。

## 依赖

* __ffmpeg 4.1.1__ 针对Linux系统

* __ffmpeg 4.1.3__ 针对Mac系统

### 安装基于Linux的FFmpeg

* 安装
```bash
$ sudo apt-get install ffmpeg
```

* 更新（如果适用）
```bash
# 截止2019年4月11日，FFmpeg的最新版本为4.x.x。
$ sudo add-apt-repository ppa:jonathonf/ffmpeg-4
$ sudo apt update && sudo apt upgrade
```

### 安装基于Mac的FFmpeg

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

## 使用

参考程序注释，设置输入和输出的媒体文件名或路径。

### 视频和音频处理

- 运行`run_VAP_extract.py`，**提取**视频中的音频。

- 运行`run_VAP_add.py`，**添加**音频到不含音频的视频。

- 运行`run_VAP_remove.py`，**删除**视频中的音频。

- 运行`run_VAP_convert.py`，**转换**音频的格式。

### 视频和音频剪辑

- **【新】** 运行`run_VAE_Video_01Clip.py`或`run_VAE_Audio_01Clip.py`，**剪切**视频或音频为片段。

- **【新】** 运行`run_VAE_Video_02Merge.py`或`run_VAE_Audio_02Merge.py`，**拼接**视频或音频的片段。


<br>

<i>如果该程序对您有帮助，请为该程序加星支持哈，非常感谢。^_^</i>

<i>最后更新：15/04/2019</i>
