import constants
import interval
import note
import scale

class Chord(object):
    def __init__(self, tonic_note, chord_number, chord_type):
        # Validate tonic_note
        if not isinstance(tonic_note, note.Note):
            raise TypeError(f"Expected Note object for tonic_note, got {tonic_note}")

        # Validate chord_number
        if not isinstance(chord_number, str):
            raise TypeError(f"Expected string for chord_number, got {chord_number}")
        if chord_number not in constants.CHORD_NUM_SCALE_INDEX:
            raise ValueError(f"Invalid chord_number: {chord_number}")
        self.chord_number = chord_number

        # Validate chord_type
        if not isinstance(chord_type, str):
            raise TypeError(f"Expected string for chord_type, got {chord_type}")
        if chord_type not in constants.CHORD_TYPE_MAP:
            raise ValueError(f"Invalid chord_type: {chord_type}")
        self.chord_type = chord_type

        self.tonic_note = tonic_note
        self.notes = []

        tonic_scale = scale.Scale(tonic_note, "major")
        tonic_scale_notes = tonic_scale.notes
        tonic_index = constants.CHORD_NUM_SCALE_INDEX[self.chord_number]
        self.notes.append(tonic_scale_notes[tonic_index])

        interval_type_tuple = constants.CHORD_TYPE_MAP[self.chord_type]
        for interval_type in interval_type_tuple:
            interval_obj = interval.Interval(interval_type)
            next_note = self.notes[-1].add_interval(interval_obj)
            self.notes.append(next_note)

    @classmethod
    def build_chord(cls, tonic_key, chord_number, chord_type, scale_type='major'):
        tonic_note = Note.from_note_string(tonic_key)
        tonic_scale = Scale(tonic_note, scale_type)
        scale_index = CHORD_NUM_SCALE_INDEX[chord_number]
        chord_tones = []
        for interval in CHORD_TYPE_MAP[chord_type]:
            chord_tones.append(tonic_scale[scale_index])
            scale_index += interval
        return cls(chord_tones)

