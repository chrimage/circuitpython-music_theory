# chord.py
from .note import Note
from .scale import Scale
from .interval import Interval

class Chord:
    _MAJOR = (2, 4)
    _MINOR = (2, 4)
    _CHORD_PATTERNS = {'major': _MAJOR, 'maj': _MAJOR, 'minor': _MINOR, 'min': _MINOR}
    _CHORD_NUM_SCALE_INDEX = {'I': 0, 'II': 1, 'III': 2, 'IV': 3, 'V': 4, 'VI': 5, 'VII': 6, 'VIII': 7}

    def __init__(self, root_note):
        if not isinstance(root_note, Note):
            raise TypeError(f"Expected Note for root note, got '{root_note}'")
        self.notes = [root_note]

    @classmethod
    def build_chord(cls, tonic_key, chord_number, chord_type):
        if not isinstance(tonic_key, Note):
            raise TypeError(f"Expected Note for tonic key, got '{tonic_key}'")
