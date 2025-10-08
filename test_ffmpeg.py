from ffmpeg import *

# Path to your Desktop folder (forward slashes)
desktop_path = "C:/Users/tarun meena/Desktop"

# Convert video from MOV to MP4
convert_video(f"{desktop_path}/input.mp4", f"{desktop_path}/output.mp4")

# Extract audio from video
extract_audio(f"{desktop_path}/input.mp4", f"{desktop_path}/audio.mp3")

# Split video into 15-second chunks
split_video(f"{desktop_path}/input.mp4", segment_time=15)

# Merge video chunks
chunks = [
    f"{desktop_path}/part_000.mp4",
    f"{desktop_path}/part_001.mp4",
    f"{desktop_path}/part_002.mp4"
]
merge_videos(chunks, f"{desktop_path}/merged.mp4")

# Extract a thumbnail at 5 seconds
extract_thumbnail(f"{desktop_path}/input.mp4", "00:00:05", f"{desktop_path}/thumb.jpg")

# Compress video
compress_video(f"{desktop_path}/input.mp4", f"{desktop_path}/compressed.mp4", crf=28, preset="medium")

# Remove audio from video
remove_audio(f"{desktop_path}/input.mp4", f"{desktop_path}/no_audio.mp4")

# Convert video to HLS
convert_to_hls(f"{desktop_path}/input.mp4", output_folder=f"{desktop_path}/hls_output")

# Cut a clip from 1:00 to 1:30
cut_clip(f"{desktop_path}/input.mp4", "00:01:00", "00:01:30", f"{desktop_path}/clip.mp4")

generate_short_clips(f"{desktop_path}/input.mp4", clip_duration=30)

extract_subtitles(f"{desktop_path}/input.mp4", f"{desktop_path}/subtitles.srt")

extract_audio_for_transcript(f"{desktop_path}/input.mp4", f"{desktop_path}/audio_for_transcript.wav")
