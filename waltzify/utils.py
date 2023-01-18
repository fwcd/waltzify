from functools import reduce
from pydub import AudioSegment

def join_audio(segments: list[AudioSegment]) -> AudioSegment:
    return reduce(lambda s1, s2: s1 + s2, segments)
