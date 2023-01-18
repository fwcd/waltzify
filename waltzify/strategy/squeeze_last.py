from pydub import AudioSegment
from pydub.effects import speedup

from waltzify.strategy import Strategy
from waltzify.utils import join_audio

class SqueezeLastStrategy(Strategy):
    '''Squeezes the last `bar_size - n` beats into the last beat.'''

    def __init__(self, n: int=2):
        self.n = n

    def waltzify_bar(self, beats: list[AudioSegment]) -> AudioSegment:
        initial = join_audio(beats[:self.n])
        last = speedup(join_audio(beats[self.n:]), playback_speed=(len(beats) - self.n), chunk_size=10, crossfade=5)
        return initial + last
