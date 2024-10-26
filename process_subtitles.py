import os
import subprocess

def extract_subtitles(video_file, srt_file):
    # Extract subtitles using ffmpeg
    subprocess.run(['ffmpeg', '-i', video_file, srt_file], check=True)
    print(f"Extracted subtitles to {srt_file}")

def add_subtitles(video_file, srt_file, output_file):
    # Add cleaned subtitles to the video using ffmpeg
    subprocess.run(['ffmpeg', '-i', video_file, '-vf', f"subtitles={srt_file}", '-c:a', 'copy', output_file], check=True)
    print(f"Added cleaned subtitles to {output_file}")

def clean_and_delete_srt(srt_file, remove_lines):
    with open(srt_file, 'r') as file:
        original_content = file.read()

    cleaned_content = clean_subtitles(original_content, remove_lines)
    
    with open(srt_file, 'w') as file:
        file.write(cleaned_content)
        
    print(f"Cleaned SRT file: {srt_file}")

def clean_subtitles(content, remove_lines):
    entries = content.split('\n\n')
    cleaned_entries = []

    for entry in entries:
        if entry.strip() == '':
            continue
        parts = entry.split('\n')
        if len(parts) >= 3:
            timestamps = parts[1].strip()
            text_lines = parts[2:]
            cleaned_text = '\n'.join(line for line in text_lines if line.strip() not in remove_lines)
            if cleaned_text.strip() != '':
                cleaned_entries.append(f'{parts[0]}\n{timestamps}\n{cleaned_text}')

    return '\n\n'.join(cleaned_entries)

def process_directory(directory, remove_lines_file, log_file):
    with open(remove_lines_file, 'r') as file:
        remove_lines = set([line.strip() for line in file.readlines()])

    if os.path.exists(log_file):
        with open(log_file, 'r') as file:
            processed_files = set([line.strip() for line in file.readlines()])
    else:
        processed_files = set()

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.mp4', '.mkv', '.avi')):
                video_file = os.path.join(root, file)
                srt_file = os.path.splitext(video_file)[0] + '.srt'
                output_file = os.path.splitext(video_file)[0] + '_cleaned.mp4'
                
                if video_file not in processed_files:
                    extract_subtitles(video_file, srt_file)
                    clean_and_delete_srt(srt_file, remove_lines)
                    add_subtitles(video_file, srt_file, output_file)
                    processed_files.add(video_file)

    with open(log_file, 'w') as file:
        for processed_file in processed_files:
            file.write(f"{processed_file}\n")

process_directory('/app/subtitles', '/app/remove_lines.txt', '/app/log/processed_files.log')


