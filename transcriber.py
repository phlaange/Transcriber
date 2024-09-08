import os
import subprocess
import configparser


# Initialize the config parser
config = configparser.ConfigParser()

# Read the configuration file
config.read('transcriber.ini')

# Retrieve 'vosk_model_path' and 'root_directory' from the 'Settings' section of the .ini file
vosk_model_path = os.path.normpath(config.get('Settings', 'vosk_model_path'))
videos_directory = os.path.normpath(config.get('Settings', 'videos_directory'))

# Recursively search through the directory structure
for folder_name, subfolders, filenames in os.walk(videos_directory):
    for filename in filenames:
        # Check if the file is an .mp4 file
        if filename.endswith('.mp4'):
            mp4_path = os.path.join(folder_name, filename)

            # Construct the .vtt file path
            vtt_path = os.path.splitext(mp4_path)[0] + '.vtt'

            # Check if the .vtt file already exists
            if not os.path.exists(vtt_path):
                # If the .vtt file does not exist, run the vosk-cli command
                try:
                    print(f"Processing: {mp4_path}")
                    subprocess.run(
                        [
                            "vosk-cli",
                            "-m", vosk_model_path,
                            "-i", mp4_path,
                            "-o", vtt_path
                        ],
                        check=True
                    )
                except subprocess.CalledProcessError as e:
                    print(f"Error processing {mp4_path}: {e}")
            else:
                print(f"Already processed: {mp4_path}")
