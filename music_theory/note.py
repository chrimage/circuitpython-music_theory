import math
from .interval import Interval
from .constants import NAMED_INTERVAL_TYPES, VALID_INTERVAL_TYPES, VALID_PITCHES, VALID_ACCIDENTALS, ACCIDENTAL_MAP, PITCH_ACCIDENTAL_MAP

class Note(object):
    def __init__(self, pitch, octave, accidental=None):
        # Validate pitch
        if not isinstance(pitch, str):
            raise TypeError(f"Expected string for pitch, got {pitch}")
        if pitch.upper() not in VALID_PITCHES:
            raise ValueError(f"Invalid pitch: {pitch}")

        # Validate octave
        try:
            octave = int(octave)
        except ValueError:
            raise TypeError(f"Expected integer for octave, got {octave}")
        if octave < 0:
            raise ValueError(f"Expected octave to be non-negative, got {octave}")

        # Validate accidental
        if accidental is not None:
            if not isinstance(accidental, str):
                raise TypeError(f"Expected string for accidental, got {accidental}")
            if accidental not in VALID_ACCIDENTALS:
                raise ValueError(f"Invalid accidental: {accidental}")

        self.pitch = pitch
        self.octave = octave
        self.accidental = accidental

    @classmethod
    def from_pitch_name(cls, pitch_name):
        if not isinstance(pitch_name, str):
            raise TypeError(f"Expected string for pitch name, got {pitch_name}")
        if pitch_name not in PITCH_ACCIDENTAL_MAP:
            raise ValueError(f"Invalid pitch name: {pitch_name}")
        pitch, accidental = PITCH_ACCIDENTAL_MAP[pitch_name]
        return cls(pitch, 0, accidental)

    @classmethod
    def transpose(self, interval):
    # Validate interval
    if not isinstance(interval, Interval):
        raise TypeError(f"Expected Interval for interval, got {interval}")

    # Calculate new pitch and octave
    pitch_index = VALID_PITCHES.index(self.pitch)
    new_pitch_index = (pitch_index + interval.semitones) % len(VALID_PITCHES)
    new_pitch = VALID_PITCHES[new_pitch_index]
    new_octave = self.octave
    if interval.semitones > 0:
        new_octave += (pitch_index + interval.semitones) // len(VALID_PITCHES)
    elif interval.semitones < 0:
        new_octave += (pitch_index + interval.semitones) // len(VALID_PITCHES) - 1

    # Calculate new accidental
    new_accidental = self.accidental
    if new_accidental is None:
        if interval.interval_type in ('M', 'P'):
            # No change needed
            pass
        elif interval.interval_type == 'm':
            new_accidental = 'b'
        elif interval.interval_type == 'aug':
            new_accidental = '#'
    else:
        if interval.interval_type in ('M', 'P'):
            # No change needed
            pass
        elif interval.interval_type == 'm':
            if new_accidental == '#':
                new_accidental = 'b'
            else:
                new_accidental = None

    def __str__(self):
        pitch_str = self.pitch
        if self.accidental is not None:
            pitch_str += self.accidental
        if self.octave > 0:
            pitch_str += str(self.octave)
        return pitch


class Rest(object):
    def __init__(self, duration):
        # Validate duration
        try:
            duration = int(duration)
        except ValueError:
            raise TypeError(f"Expected integer for duration, got {duration}")
        if duration <= 0:
            raise ValueError(f"Expected duration to be positive, got {duration}")
        self.duration = duration

    def __str__(self):
        return 'rest'
