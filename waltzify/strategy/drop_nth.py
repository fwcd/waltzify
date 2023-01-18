from pydub import AudioSegment
from pydub.effects import speedup

from waltzify.strategy import Strategy
from waltzify.utils import join_audio

class DropNthStrategy(Strategy):
    '''Removes the `n`th beat (and then as many as required to make the bar 3/4).'''

    def __init__(self, n: int):
        self.n = n

    def waltzify_bar(self, beats: list[AudioSegment]) -> AudioSegment:
        dropped = len(beats) - 3
        return join_audio(beats[:self.n] + beats[self.n + dropped:])
