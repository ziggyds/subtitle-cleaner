# Subtitle Cleaner

This project automates the process of cleaning subtitles.

## Features

- Extracts subtitles from video files using `ffmpeg`.
- Cleans subtitles.
- Re-adds cleaned subtitles to video files using `ffmpeg`.
- Keeps track of processed files to avoid re-processing.
- Runs periodically based on a specified interval using Docker.

## Prerequisites

- Docker installed on your system.

## Usage

1. **Prepare your subtitle and video files**:
    Create a `remove_lines.txt` file with lines to be removed.

2. **Run the Docker container**:
    ```sh
    docker run -e "INTERVAL=30m" -v /path/to/subtitles:/app/subtitles -v /path/to/log:/app/log -v /path/to/remove_lines.txt:/app/remove_lines.txt subtitle-cleaner
    ```
    - `INTERVAL`: Set the interval for running the script (e.g., `10m`, `30m`, `1h`, `1d`, `1w`).
    - `/path/to/subtitles`: Directory containing your video and subtitle files.
    - `/path/to/log`: Directory where `processed_files.log` will be saved.
    - `/path/to/remove_lines.txt`: File containing lines to be removed.
