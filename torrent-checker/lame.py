"""Module for converting FLAC files to MP3 using LAME."""


def convert_flac_to_mp3(input_file, output_file):
    """Convert a FLAC file to MP3 using LAME."""
    import subprocess

    command = ["lame", "--mp3input", "--cbr", "--abr", "320", input_file, output_file]

    try:
        subprocess.run(command, check=True)
        print(f"Converted {input_file} to {output_file} successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")


def is_flac_file(file_path):
    """Check if the file is a FLAC file."""
    return file_path.lower().endswith(".flac")
