# YTConverter

YTConverter is a very simple YouTube Downloader, capable of converting
YouTube Videos into MP3, MP4 and WAV formats.

## Install

- Clone this repository into a directory of your choice.
- Create a virtual environment through running `py -m venv .venv` in a
terminal of your choice.
- Activate the virtual environment through running `.venv\Scripts\activate`.
If you are running on a Linux Machine, you'll need to run
`source venv/bin/activate` instead.
- Install the dependencies for this project through running
`pip install -r requirements.txt`.

You should now be all good to use the project!

## Usage

Running the script requires a URL and a specified filetype.
You may only specify one filetype at this time.

To convert a Video to MP3, run:
```
py YTConverter.py <URL> --mp3
```

To convert a Video to MP3, run:
```
py YTConverter.py <URL> --mp4
```

To convert a Video to MP3, run:
```
py YTConverter.py <URL> --wav
```