# Music Theory for CircuitPython

This library provides classes for working with musical concepts in CircuitPython.

## Classes

### Interval

`Interval` represents a musical interval between two pitches.

#### Methods

- `from_interval_string(cls, interval_string)`: creates an `Interval` object from a string representation of the interval.
- `from_semitones(cls, semitones)`: creates an `Interval` object from a number of semitones.

### Note

`Note` represents a single pitch with a pitch name, octave, and optional accidental.

#### Methods

- `from_note_string(cls, note_string)`: creates a `Note` object from a string representation of the pitch.
- `from_midi_num(cls, midi_num)`: creates a `Note` object from a MIDI number.

### Scale

`Scale` represents a series of pitches organized in a specific pattern of intervals.

#### Methods

- `build_scale(cls, tonic, scale_type)`: creates a `Scale` object starting from the given `tonic` `Note` and using the given `scale_type` string.

### Chord

`Chord` represents a group of pitches that form a chord.

#### Methods

- `build_chord(cls, tonic_key, chord_number, chord_type)`: creates a `Chord` object starting from the given `tonic_key` `Note` and using the given `chord_number` and `chord_type` strings.

## Example

Here's an example of how to use the `MusicTheory` library to build and play a C major chord:

```python
import adafruit_midi
from music_theory import Chord, Note

# Set up MIDI
midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[0])

# Build a C major chord
tonic = Note.from_note_string("C4")
chord = Chord.build_chord(tonic, "I", "major")

# Play the chord
for note in chord.notes:
    note_number = note.to_number()
    midi.send(adafruit_midi.NoteOn(note_number, 64))

```
