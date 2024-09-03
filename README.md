# Audio Cutter Script

This repository contains a Python script that allows you to cut specific segments from audio files. 
The script was originally developed to process `.webm` files but is flexible enough to handle any audio format supported by the `pydub` library, such as `.mp3`, `.wav`, `.ogg`, and others.

## Key Sections:
- **Project Overview**: Describes the purpose of the script and its features.
- **Requirements**: Lists the necessary dependencies, including Python, `pydub`, and FFmpeg, with a link to FFmpeg's official installation page.
- **Installation Instructions**: Guides the user through setting up the script, including cloning the repository and installing dependencies.
- **Usage**: Provides instructions on how to configure and run the script, including an example setup.
- **Supported Formats**: Lists the audio formats that the script can handle.
- **License & Contributions**: Information on the project's license and how to contribute.

## Project Overview
The Audio Cutter Script is a versatile tool designed to extract specific segments from audio files. 
Initially conceived as a utility to handle .webm files, this project has evolved to support a wide range of audio formats compatible with the pydub library, including .mp3, .wav, .ogg, and more.

The script is particularly useful for tasks that require batch processing of audio files, such as creating snippets or removing unwanted sections from multiple files at once. 
By specifying start and end times, users can quickly and efficiently cut portions of audio files without the need for manual editing.

This script leverages the power of FFmpeg, a leading multimedia framework, for processing audio data. 
It allows you to work with various audio formats, making it a flexible solution for diverse audio processing needs.

**Key features include:**

- Support for Multiple Audio Formats: Originally developed for .webm files, the script now handles any format supported by pydub and FFmpeg.
- Batch Processing: Automatically process all audio files in a specified directory, saving time and effort.
- Customizable Parameters: Users can easily specify input/output directories, start/end times for cutting, and the desired file format.
- Whether you need to trim audio files for a podcast, extract music samples, or prepare audio for analysis, this script provides a straightforward solution.

## Requirements

Before running the script, make sure you have the following installed:

- **Python 3.x**: This script is written in Python and requires Python 3.x to run.
- **pydub Library**: Used for audio processing.
- **FFmpeg**: The script relies on FFmpeg for reading and writing audio files. To install FFmpeg, follow the instructions on the official FFmpeg website https://ffmpeg.org/download.html.

## Installation Instruccions

**Clone the Repository:**

bash

    git clone https://github.com/yourusername/audiocutter.git
    cd audiocutter

**Install Required Python Packages:**

bash

    pip install -r requirements.txt

**Download and Install FFmpeg**

Visit the official FFmpeg website for installation instructions.
After installing, make sure to update the paths to the ffmpeg and ffprobe binaries in the script:

python

    AudioSegment.ffmpeg = r"C:\path\to\ffmpeg.exe"
  
    AudioSegment.ffprobe = r"C:\path\to\ffprobe.exe"

## Usage

**1. Customize the Script:**

- Open the script and replace the placeholder paths with your actual directories.
- Set the start_time and end_time for the segment you want to cut.
- Specify the file_extension of the audio files you want to process.

**2. Run the Script:**

    python your_script_name.py

Output:

-  The processed files will be saved in the specified output directory with a cut_ prefix.

**3. Example**

Here’s an example of how to set up the script:

python

    input_dir = r"C:\path\to\input\directory"
    
    output_dir = r"C:\path\to\output\directory"
    
    start_time = "00:30"  # Start time in MM:SS or HH:MM:SS format
    
    end_time = "02:00"    # End time in MM:SS or HH:MM:SS format
    
    file_extension = ".mp3"  # The extension of the files you want to process


## Supported Formats

The script supports any audio format that the pydub library and FFmpeg can handle. Some of the common formats include:

- .webm
- .mp3
- .wav
- .ogg
- .flv
- .aac

## Licence & Contributions

This project is licensed under the MIT License. See the LICENSE file for details.

**Contributions**
Contributions are welcome! Please open an issue or submit a pull request with your improvements.

**Acknowledgments**
This project was started as a simple script to cut .webm files but has evolved to support multiple audio formats thanks to the flexibility of the pydub library and FFmpeg.
