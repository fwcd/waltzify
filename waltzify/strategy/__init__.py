from pydub import AudioSegment

class Strategy:
    def waltzify_bar(self, beats: list[AudioSegment]) -> AudioSegment:
        raise NotImplementedError(f'waltzify has not been implemented for {type(self).__name__}')
