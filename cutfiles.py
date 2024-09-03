import os
from pydub import AudioSegment
from datetime import timedelta

AudioSegment.ffmpeg = r"C:\ffmpeg\bin\ffmpeg.exe" #the path where you have installed ffmpeg
AudioSegment.ffprobe = r"C:\ffmpeg\bin\ffprobe.exe"  #the path where you have installed ffmpeg

def cut_audio(input_file, output_file, start_time, end_time, format):
    # Load audio file based on the specified format
    audio = AudioSegment.from_file(input_file, format=format)
    start_ms = start_time * 1000
    end_ms = end_time * 1000
    cut_audio = audio[start_ms:end_ms]
    cut_audio.export(output_file, format=format)

def time_to_seconds(time_str):
    if ':' in time_str:
        time_parts = list(map(int, time_str.split(':')))
        if len(time_parts) == 2:
            return timedelta(minutes=time_parts[0], seconds=time_parts[1]).total_seconds()
        elif len(time_parts) == 3:
            return timedelta(hours=time_parts[0], minutes=time_parts[1], seconds=time_parts[2]).total_seconds()
    else:
        return float(time_str)

def process_directory(input_dir, output_dir, start_time, end_time, file_extension):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    start_seconds = time_to_seconds(start_time)
    end_seconds = time_to_seconds(end_time)

    for filename in os.listdir(input_dir):
        if filename.endswith(file_extension):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f"cut_{filename}")
            print(f"Processing file: {input_path}")
            #audio = AudioSegment.from_file(input_path, format=format)
            cut_audio(input_path, output_path, start_seconds, end_seconds, file_extension.strip('.'))
            print(f"Processed {filename}")

def main():
    input_dir = r"Your input files directory"
    output_dir = r"The output directory for your cut files"    
    start_time = "xx:xx" #mm:ss
    end_time = "xx:xx" #mm:ss
    file_extension = ".???" #the extension of your file, .webm , .mp3, etc

    process_directory(input_dir, output_dir, start_time, end_time, file_extension)
    print(f"All {file_extension} files have been processed.")

if __name__ == "__main__":
    main()
