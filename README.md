# FFmpeg Python Utility

A Python wrapper for **FFmpeg** created by **Tarun Meena** that simplifies common video and audio processing tasks with **detailed logging**. This utility allows you to automate video conversions, splitting, merging, thumbnail extraction, compression, audio extraction, and more—all from Python scripts.  

---

## **GitHub Repository**

[https://github.com/Tarunmeena656/ffmpeg-code](https://github.com/Tarunmeena656/ffmpeg-code)

---

## **Features**

### Basic Video & Audio Operations
- **Convert video formats**  
  Convert between `.mov`, `.mp4`, `.avi`, etc.  
  `convert_video(input_file, output_file)`

- **Extract audio**  
  Extract audio from video in `.mp3` format.  
  `extract_audio(input_file, output_audio)`

- **Split video into segments**  
  Split videos into smaller segments for easier processing.  
  `split_video(input_file, segment_time, output_pattern)`

- **Merge videos**  
  Merge multiple video files into a single file. Requires all videos to have the same codec and resolution.  
  `merge_videos(file_list, output_file)`

- **Extract thumbnails**  
  Capture a frame from the video at a specific timestamp.  
  `extract_thumbnail(input_file, timestamp, output_image)`

- **Compress video**  
  Reduce file size using H.264 compression and adjustable quality.  
  `compress_video(input_file, output_file, crf, preset)`

- **Remove audio**  
  Strip audio from a video file.  
  `remove_audio(input_file, output_file)`

- **Convert to HLS**  
  Generate HLS streaming segments (`.m3u8`) and `.ts` chunks.  
  `convert_to_hls(input_file, output_folder, segment_time)`

- **Cut video clip**  
  Extract a portion of the video without re-encoding.  
  `cut_clip(input_file, start, end, output_file)`

---

### Advanced / New Functions
- **Generate short clips automatically**  
  Split a video into multiple short clips of specified duration.  
  `generate_short_clips(input_file, clip_duration, output_pattern)`

- **Extract subtitles**  
  Extract embedded subtitles from video in `.srt` format.  
  `extract_subtitles(input_file, output_file)`

- **Extract audio for transcription**  
  Extract audio in **16kHz mono WAV** format for speech-to-text or transcription.  
  `extract_audio_for_transcript(input_file, output_audio)`

---

## **Installation**

1. Install **FFmpeg** and make sure it is available in your system PATH:  
   [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)

2. Ensure Python 3.8+ is installed.

3. Clone this repository:

```bash
git clone https://github.com/Tarunmeena656/ffmpeg-code.git
cd ffmpeg-code

from ffmpeg import *

# -------------------- Path Setup --------------------
desktop_path = "C:/Users/tarun meena/Desktop"
test_video = f"{desktop_path}/test_ffmpeg_file.mp4"  # Sample video for testing

# -------------------- Test Only --------------------
# Only uncomment the functions you want to test

# Convert video (if you want to test conversion)
# convert_video(test_video, f"{desktop_path}/output_test.mp4")

# Extract audio for transcript
extract_audio_for_transcript(test_video, f"{desktop_path}/audio_for_transcript_test.wav")

# Generate short clips
generate_short_clips(test_video, clip_duration=10, output_pattern=f"{desktop_path}/clip_test_%03d.mp4")

# Extract subtitles (if available)
extract_subtitles(test_video, f"{desktop_path}/subtitles_test.srt")

# -------------------- Commented Out --------------------
# Other functions are commented to avoid unnecessary execution
# convert_video(...)
# extract_audio(...)
# split_video(...)
# merge_videos(...)
# extract_thumbnail(...)
# compress_video(...)
# remove_audio(...)
# convert_to_hls(...)
# cut_clip(...)
