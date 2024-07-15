# Imports
import os
import argparse
from yt_dlp import YoutubeDL

# Make sure output dir exists,
output_dir = os.path.join(os.getcwd(), "output")
os.makedirs(output_dir, exist_ok=True)

# Download WAV function.
def download_wav(youtube_url: str) -> None:
    ytdl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "wav"
        }],
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s")
    }
    with YoutubeDL(ytdl_opts) as ydl:
        ydl.download([youtube_url])

# Download MP3 function.
def download_mp3(youtube_url: str) -> None:
    ytdl_opts = {
        "format": "mp3/bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3"
        }],
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s")
    }
    with YoutubeDL(ytdl_opts) as ydl:
        ydl.download([youtube_url])

# Download MP4 function.
def download_mp4(youtube_url: str) -> None:
    ytdl_opts = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s")
    }
    with YoutubeDL(ytdl_opts) as ydl:
        ydl.download([youtube_url])

# Main function.
def main():
    parser = argparse.ArgumentParser(description="Download YouTube videos as MP3 or MP4.")
    parser.add_argument("youtube_url", type=str, help="URL of the YouTube video to download.")
    parser.add_argument("--mp3", action="store_true", help="Download as MP3.")
    parser.add_argument("--mp4", action="store_true", help="Download as MP4.")
    parser.add_argument("--wav", action="store_true", help="Download as WAV.")
    args = parser.parse_args()
    if args.mp3 and args.mp4:
        raise ValueError("Only one of --mp3 or --mp4 can be specified.")
    if args.mp3:
        download_mp3(args.youtube_url)
    elif args.mp4:
        download_mp4(args.youtube_url)
    elif args.wav:
        download_wav(args.youtube_url)
    else:
        raise ValueError("One of --mp3 or --mp4 must be specified.")

# Run main function.
if __name__ == "__main__":
    main()