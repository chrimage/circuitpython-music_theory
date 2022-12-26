# Music Theory for CircuitPython

## Classes

### Interval

- `Interval` represents a musical interval between two pitches.
- It has the following class methods:
  - `from_interval_string(cls, interval_string)`: creates an `Interval` object from a string representation of the interval.
  - `from_semitones(cls, semitones)`: creates an `Interval` object from a number of semitones.

### Note

- `Note` represents a single pitch with a pitch name, octave, and optional accidental.
- It has the following class methods:
  - `from_note_string(cls, note_string)`: creates a `Note` object from a string representation of the pitch.
  - `from_midi_num(cls, midi_num)`: creates a `Note` object from a MIDI number.

### Scale

- `Scale` represents a series of pitches organized in a specific pattern of intervals.
- It has the following class method:
  - `build_scale(cls, tonic, scale_type)`: creates a `Scale` object starting from the given `tonic` `Note` and using the given `scale_type` string.

### Chord

- `Chord` represents a group of pitches that form a chord.
- It has the following class method:
  - `build_chord(cls, tonic_key, chord_number, chord_type)`: creates a `Chord` object starting from the given `tonic_key` `Note` and using the given `chord_number` and `chord_type` strings.
