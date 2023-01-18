from pathlib import Path
from pydub import AudioSegment

import argparse

def main():
    parser = argparse.ArgumentParser(description='Converts a 4/4 song to 3/4')
    parser.add_argument('--output', '-o', required=True, type=Path, help='The output (audio) file path.')
    parser.add_argument('input', type=Path, help='The input (audio) file path.')

    args = parser.parse_args()

    audio = AudioSegment.from_file(args.input)
    audio.export(args.output)
