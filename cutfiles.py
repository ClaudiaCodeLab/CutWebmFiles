import os
from pydub import AudioSegment
from datetime import timedelta

# Set the path to your installed ffmpeg and ffprobe binaries.
AudioSegment.ffmpeg = r"C:\ffmpeg\bin\ffmpeg.exe"
AudioSegment.ffprobe = r"C:\ffmpeg\bin\ffprobe.exe"

def cut_audio(input_file, output_file, start_time, end_time, format):
    """Cuts a segment from an audio file and exports it to a new file.

    Args:
        input_file (str): The path to the input audio file.
        output_file (str): The path where the output audio file will be saved.
        start_time (float): The start time of the segment to cut, in seconds.
        end_time (float): The end time of the segment to cut, in seconds.
        format (str): The format of the audio file (e.g., 'mp3', 'wav').
    """
    # Load the audio file in the specified format.
    audio = AudioSegment.from_file(input_file, format=format)
    
    # Convert start and end times from seconds to milliseconds.
    start_ms = start_time * 1000
    end_ms = end_time * 1000
    
    # Slice the audio file to keep only the portion between start and end times.
    cut_audio = audio[start_ms:end_ms]
    
    # Export the sliced audio to the output file in the specified format.
    cut_audio.export(output_file, format=format)

def time_to_seconds(time_str):
    """Converts a time string (HH:MM:SS or MM:SS) into seconds.

    Args:
        time_str (str): A string representing time in HH:MM:SS or MM:SS format.

    Returns:
        float: The total number of seconds represented by the input time string.
    """
    # Check if the time string contains ':', indicating it's in HH:MM:SS or MM:SS format.
    if ':' in time_str:
        # Split the time string into its components (hours, minutes, seconds).
        time_parts = list(map(int, time_str.split(':')))
        
        # If the format is MM:SS, convert to seconds.
        if len(time_parts) == 2:
            return timedelta(minutes=time_parts[0], seconds=time_parts[1]).total_seconds()
        
        # If the format is HH:MM:SS, convert to seconds.
        elif len(time_parts) == 3:
            return timedelta(hours=time_parts[0], minutes=time_parts[1], seconds=time_parts[2]).total_seconds()
    
    # If the time string does not contain ':', assume it is in seconds and return as float.
    else:
        return float(time_str)

def process_directory(input_dir, output_dir, start_time, end_time, file_extension):
    """Processes all audio files in a directory, cutting each based on specified start and end times.

    Args:
        input_dir (str): The directory containing the input audio files.
        output_dir (str): The directory where the processed audio files will be saved.
        start_time (str): The start time for the segment to cut (HH:MM:SS or MM:SS).
        end_time (str): The end time for the segment to cut (HH:MM:SS or MM:SS).
        file_extension (str): The extension of the audio files to process (e.g., '.mp3', '.wav').
    """
    # Create the output directory if it does not exist.
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Convert start and end times to seconds.
    start_seconds = time_to_seconds(start_time)
    end_seconds = time_to_seconds(end_time)

    # Loop through all files in the input directory.
    for filename in os.listdir(input_dir):
        # Check if the file has the specified extension.
        if filename.endswith(file_extension):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f"cut_{filename}")
            print(f"Processing file: {input_path}")
            
            # Call the cut_audio function to slice and save the audio.
            cut_audio(input_path, output_path, start_seconds, end_seconds, file_extension.strip('.'))
            print(f"Processed {filename}")

def main():
    """Main function to set parameters and process the audio files."""
    # Replace with your input directory path.
    input_dir = r"Your input files directory"
    
    # Replace with your output directory path.
    output_dir = r"The output directory for your cut files"
    
    # Start time of the audio segment you want to keep (format: MM:SS or HH:MM:SS).
    start_time = "00:00"  # Example: "00:30" for 30 seconds or "01:15" for 1 minute 15 seconds
    
    # End time of the audio segment you want to keep (format: MM:SS or HH:MM:SS).
    end_time = "00:00"  # Example: "02:00" for 2 minutes
    
    # The extension of your audio files (e.g., ".mp3", ".wav", ".webm").
    file_extension = ".mp3"  # Example: ".mp3", ".wav", etc.

    # Call the process_directory function to process all files in the directory.
    process_directory(input_dir, output_dir, start_time, end_time, file_extension)
    print(f"All {file_extension} files have been processed.")

if __name__ == "__main__":
    main()