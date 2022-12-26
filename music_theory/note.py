import random
import math
from .interval import Interval

class Note:
    VALID_PITCHES = ('C', 'D', 'E', 'F', 'G', 'A', 'B')
    VALID_ACCIDENTALS = ('#', '##', 'b', 'bb', None)

    def __init__(self, pitch, octave, accidental=None, random_instance=random.Random()):
        if not isinstance(pitch, str):
            raise TypeError(f"Expected string for pitch, got: {pitch}")
        if pitch.upper() not in Note.VALID_PITCHES:
            raise ValueError(f"Invalid pitch: {pitch}")
        if not isinstance(octave, int):
            raise TypeError(f"Expected integer for octave, got: {octave}")
        if octave < -1 or octave > 9:
            raise ValueError(f"Octave needs to be in the range [-1, 9], got: {octave}")
        if accidental is not None and accidental.lower() not in Note.VALID_ACCIDENTALS:
            raise ValueError(f"Invalid accidental: {accidental}")
        self.pitch = pitch.upper()
        self.octave = octave
        self.accidental = accidental
        self.is_rest = False
        self.random_instance = random_instance
        if accidental is not None:
            self.accidental = self.accidental.lower()
        if self.midi_note_number() < 0 or self.midi_note_number() > 127:
            raise ValueError(f"Invalid Note parameters '{self.pitch}{self.octave}{self.accidental}', results in MIDI note number: {self.midi_note_number()}")

    @classmethod
    def from_note_string(cls, note_string, random_instance=random.Random()):
        if not isinstance(note_string, str):
            raise TypeError(f"Expected string for note string, got '{note_string}'")
        if note_string == 'r':
            return Rest()
        pitch = note_string[0]
        octave = note_string[1]
        accidental = note_string[2:]
        if octave == '-':
            octave = note_string[1:3]
            accidental = note_string[3:]
        if len(accidental) == 0:
            accidental = None
        return cls(pitch, octave, accidental, random_instance)

    @classmethod
    def from_midi_num(cls, midi_num, random_instance=random.Random()):
        if not isinstance(midi_num, int):
            raise TypeError(f"Expected integer for MIDI number, got: {midi_num}")
        if midi_num < 0 or midi_num > 127:
            raise ValueError(f"MIDI number needs to be in the range [0, 127], got: {midi_num}")
        pitch_accidental_mappings = {
            0: ('C', None),
            1: ('C', None),
            2: ('D', None),
            3: ('D', '#'),
            4: ('E', None),
            5: ('F', None),
            6: ('F', '#'),
            7: ('G', None),
            8: ('G', '#'),
            9: ('A', None),
            10: ('A', '#'),
            11: ('B', None)
        }
        octave = math.floor(midi_num / 12) - 1
        pitch, accidental = pitch_accidental_mappings[midi_num % 12]
        return cls(pitch, octave, accidental, random_instance)

    def __str__(self):
        if self.is_rest:
            return 'r'
        accidental = self.accidental
        if accidental is None:
            accidental = ''
        return f"{self.pitch}{self.octave}{accidental}"

    def __eq__(self, other):
        if isinstance(other, Note):
            return self.midi_note_number() == other.midi_note_number()
        return False

    def __ne__(self, other):
        if isinstance(other, Note):
            return self.midi_note_number() != other.midi_note_number()
        return True

    def __lt__(self, other):
        if isinstance(other, Note):
            return self.midi_note_number() < other.midi_note_number()
        return False

    def __le__(self, other):
        if isinstance(other, Note):
            return self.midi_note_number() <= other.midi_note_number()
        return False

    def __gt__(self, other):
        if isinstance(other, Note):
            return self.midi_note_number() > other.midi_note_number()
        return False

    def __ge__(self, other):
        if isinstance(other, Note):
            return self.midi_note_number() >= other.midi_note_number()
        return False

    def __add__(self, other):
        if isinstance(other, Interval):
            return self.transpose(other)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Interval):
            return self.transpose(-other)
        if isinstance(other, Note):

