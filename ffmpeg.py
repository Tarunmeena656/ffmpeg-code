import subprocess
import os
from typing import List

# ------------------------- Helper -------------------------
def run_ffmpeg(cmd: List[str], task_name: str = "FFmpeg Task"):
    """
    Run ffmpeg command with logging.
    """
    print(f"\n⚙️ Running [{task_name}]:", " ".join(cmd))
    process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if process.returncode != 0:
        print(f" [{task_name}] Error:\n{process.stderr}")
    else:
        print(f" [{task_name}] Done")
    return process

# ------------------------- Basic Video Tasks -------------------------
def convert_video(input_file: str, output_file: str):
    return run_ffmpeg(["ffmpeg", "-i", input_file, output_file], "Convert Video")

def extract_audio(input_file: str, output_audio: str):
    return run_ffmpeg(["ffmpeg", "-i", input_file, "-vn", "-acodec", "libmp3lame", output_audio], "Extract Audio")

def split_video(input_file: str, segment_time: int = 15, output_pattern: str = "part_%03d.mp4"):
    cmd = [
        "ffmpeg", "-i", input_file, "-c", "copy",
        "-map", "0", "-f", "segment",
        "-segment_time", str(segment_time),
        output_pattern
    ]
    return run_ffmpeg(cmd, "Split Video")

def merge_videos(file_list: List[str], output_file: str = "merged.mp4"):
    list_path = "list.txt"
    with open(list_path, "w") as f:
        for file in file_list:
            f.write(f"file '{os.path.abspath(file)}'\n")
    cmd = ["ffmpeg", "-f", "concat", "-safe", "0", "-i", list_path, "-c", "copy", output_file]
    return run_ffmpeg(cmd, "Merge Videos")

def extract_thumbnail(input_file: str, timestamp: str = "00:00:05", output_image: str = "thumbnail.jpg"):
    cmd = ["ffmpeg", "-ss", timestamp, "-i", input_file, "-frames:v", "1", output_image]
    return run_ffmpeg(cmd, "Extract Thumbnail")

def compress_video(input_file: str, output_file: str, crf: int = 28, preset: str = "medium"):
    cmd = [
        "ffmpeg", "-i", input_file,
        "-vcodec", "libx264", "-crf", str(crf),
        "-preset", preset, "-acodec", "aac",
        output_file
    ]
    return run_ffmpeg(cmd, "Compress Video")

def remove_audio(input_file: str, output_file: str):
    cmd = ["ffmpeg", "-i", input_file, "-an", output_file]
    return run_ffmpeg(cmd, "Remove Audio")

def convert_to_hls(input_file: str, output_folder: str = "hls_output", segment_time: int = 10):
    os.makedirs(output_folder, exist_ok=True)
    output_path = os.path.join(output_folder, "index.m3u8")
    cmd = [
        "ffmpeg", "-i", input_file,
        "-profile:v", "baseline", "-level", "3.0",
        "-start_number", "0",
        "-hls_time", str(segment_time),
        "-hls_list_size", "0",
        "-f", "hls", output_path
    ]
    return run_ffmpeg(cmd, "Convert to HLS")

def cut_clip(input_file: str, start: str, end: str, output_file: str = "clip.mp4"):
    cmd = ["ffmpeg", "-ss", start, "-to", end, "-i", input_file, "-c", "copy", output_file]
    return run_ffmpeg(cmd, "Cut Clip")

# ------------------------- New Functions -------------------------
def generate_short_clips(input_file: str, clip_duration: int = 30, output_pattern: str = "clip_%03d.mp4"):
    """
    Split video into multiple short clips automatically.
    """
    cmd = [
        "ffmpeg", "-i", input_file,
        "-c", "copy",
        "-map", "0",
        "-f", "segment",
        "-segment_time", str(clip_duration),
        "-reset_timestamps", "1",
        output_pattern
    ]
    return run_ffmpeg(cmd, "Generate Short Clips")

def extract_subtitles(input_file: str, output_file: str = "subtitles.srt"):
    """
    Extract subtitles from video (if available) in SRT format.
    """
    cmd = ["ffmpeg", "-i", input_file, "-map", "0:s:0", output_file]
    return run_ffmpeg(cmd, "Extract Subtitles")

def extract_audio_for_transcript(input_file: str, output_audio: str = "transcript_audio.wav"):
    """
    Extract audio suitable for transcription (16kHz mono).
    """
    cmd = ["ffmpeg", "-i", input_file, "-ar", "16000", "-ac", "1", output_audio]
    return run_ffmpeg(cmd, "Extract Audio for Transcript")

# # ------------------------- Example Usage -------------------------
# if __name__ == "__main__":
#     desktop_path = "C:/Users/tarun meena/Desktop"
    
#     convert_video(f"{desktop_path}/input.mov", f"{desktop_path}/output.mp4")
#     extract_audio(f"{desktop_path}/input.mp4", f"{desktop_path}/audio.mp3")
#     split_video(f"{desktop_path}/input.mp4")
#     merge_videos([f"{desktop_path}/part_000.mp4", f"{desktop_path}/part_001.mp4", f"{desktop_path}/part_002.mp4"], f"{desktop_path}/merged.mp4")
#     extract_thumbnail(f"{desktop_path}/input.mp4", "00:00:05", f"{desktop_path}/thumb.jpg")
#     compress_video(f"{desktop_path}/input.mp4", f"{desktop_path}/compressed.mp4")
#     remove_audio(f"{desktop_path}/input.mp4", f"{desktop_path}/no_audio.mp4")
#     convert_to_hls(f"{desktop_path}/input.mp4", output_folder=f"{desktop_path}/hls_output")
#     cut_clip(f"{desktop_path}/input.mp4", "00:01:00", "00:01:30", f"{desktop_path}/clip.mp4")
    
#     # New functions
#     generate_short_clips(f"{desktop_path}/input.mp4", clip_duration=30)
#     extract_subtitles(f"{desktop_path}/input.mp4", f"{desktop_path}/subtitles.srt")
#     extract_audio_for_transcript(f"{desktop_path}/input.mp4", f"{desktop_path}/audio_for_transcript.wav")
