from functools import reduce
from pathlib import Path
from pydub import AudioSegment
from pydub.effects import speedup
from tqdm import tqdm

from waltzify.strategy import Strategy
from waltzify.strategy.squeeze_last import SqueezeLastStrategy
from waltzify.strategy.take_prefix import TakePrefixStrategy
from waltzify.waltzify import waltzify

import argparse

STRATEGIES: dict[str, Strategy] = {
    'take-prefix': TakePrefixStrategy(),
    'squeeze-last': SqueezeLastStrategy(),
}

def main():
    parser = argparse.ArgumentParser(description='Converts a 4/4 song to 3/4')
    parser.add_argument('--bpm', '-b', required=True, type=float, help="The input audio's beats per minute.")
    parser.add_argument('--bar-size', '-s', type=int, default=4, help="The input audio's number of beats per bar.")
    parser.add_argument('--output', '-o', type=Path, help='The output (audio) file path.')
    parser.add_argument('--strategy', type=str, default='take-prefix', choices=sorted(STRATEGIES.keys()), help='The strategy for waltzifying a bar.')
    parser.add_argument('input', type=Path, help='The input (audio) file path.')

    args = parser.parse_args()
    input: Path = args.input
    output: Path = args.output or input.parent / f'{input.stem}-waltz.mp3'
    strategy = STRATEGIES[args.strategy]

    audio = AudioSegment.from_file(input)
    audio = waltzify(
        audio,
        strategy=strategy,
        bpm=args.bpm,
        bar_size=args.bar_size
    )
    audio.export(output)
