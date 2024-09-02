# Transcriber
Transcriber is a Python scribes that transcribes the speech from videos, in a folder hierarchy, into subtitle files for those videos.

This script uses the [vosk-cli](https://github.com/elan-ev/vosk-cli), which is an interface for the [Vosk](https://alphacephei.com/vosk/) speech recognition toolkit. 

## Usage
1. Follow the directions to install [vosk-cli](https://github.com/elan-ev/vosk-cli), which should also install [Vosk](https://alphacephei.com/vosk/).
2. Install [ffmpeg](https://www.ffmpeg.org/). A convenient way to do this is with [Chris Titus Tech's Windows Utility](https://github.com/ChrisTitusTech/winutil).
2. Create a transcriber.ini file in the same folder as this script, thus:

```ini
[Settings]
videos_directory = "C:\Users\MyWindowsAcccountName\Videos"
vosk_model_path = "C:\Users\MyWindowsAcccountName\.cache\vosk\vosk-model-en-us-0.22"
```
3. The **vosk_model_path** is the path to the folder where you unzipped your chosen [Vosk Model](https://alphacephei.com/vosk/models).
4. Run the script with your favourite Python IDE/environment.