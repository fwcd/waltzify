from functools import reduce
from pathlib import Path
from pydub import AudioSegment
from pydub.effects import speedup

import argparse

def join_audio(segments: list[AudioSegment]) -> AudioSegment:
    return reduce(lambda s1, s2: s1 + s2, segments)

def waltzify(audio: AudioSegment, bpm: float, bar_size: int = 4) -> AudioSegment:
    beat_ms = int(60_000 / bpm)
    beats = list(audio[::beat_ms])
    new_beats = AudioSegment.empty()

    initial_beats = 2
    remaining_beats = bar_size - initial_beats

    # Map 1 - 2 - 3 - 4 -
    # to  1 - 2 - 3 4

    for i in range(len(beats) // bar_size):
        offset = i * bar_size
        new_beats += join_audio(beats[offset:offset + initial_beats])
        new_beats += speedup(join_audio(beats[offset + initial_beats:offset + bar_size]), playback_speed=remaining_beats, chunk_size=10, crossfade=5)

    return new_beats

def main():
    parser = argparse.ArgumentParser(description='Converts a 4/4 song to 3/4')
    parser.add_argument('--bpm', '-b', required=True, type=float, help="The input audio's beats per minute.")
    parser.add_argument('--output', '-o', type=Path, help='The output (audio) file path.')
    parser.add_argument('input', type=Path, help='The input (audio) file path.')

    args = parser.parse_args()
    input: Path = args.input
    output: Path = args.output or input.parent / f'{input.stem}-waltz.mp3'

    audio = AudioSegment.from_file(input)
    audio = waltzify(audio, bpm=args.bpm)
    audio.export(output)
