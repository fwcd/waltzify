from pydub import AudioSegment
from tqdm import tqdm

from waltzify.strategy import Strategy
from waltzify.utils import join_audio

def waltzify(audio: AudioSegment, strategy: Strategy, bpm: float, bar_size: int) -> AudioSegment:
    beat_ms = int(60_000 / bpm)
    beats = list(audio[::beat_ms])
    new_beats = AudioSegment.empty()

    for i in tqdm(range(len(beats) // bar_size)):
        offset = i * bar_size
        bar_beats = beats[offset:offset + bar_size]
        new_beats += strategy.waltzify_bar(bar_beats)

    return new_beats
