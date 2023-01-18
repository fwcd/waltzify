from pydub import AudioSegment
from pydub.effects import speedup

from waltzify.strategy import Strategy
from waltzify.utils import join_audio

class TakePrefixStrategy(Strategy):
    '''Takes the first `n` beats.'''

    def __init__(self, n: int=3):
        self.n = n

    def waltzify_bar(self, beats: list[AudioSegment]) -> AudioSegment:
        return join_audio(beats[:self.n])
