import usb_midi
import adafruit_midi
from music_theory.note import Note
from music_theory.interval import Interval
from music_theory.chord import Chord

midi = adafruit_midi.MIDI(midi_in=usb_midi.ports[0], midi_out=usb_midi.ports[1], in_channel=(1, 2, 3), out_channel=0)
print('Midi Demo in and out')
print('Default output channel:', (midi.out_channel + 1))
print('Listening on input channels:', tuple(((c + 1) for c in midi.in_channel)))

while True:
    while True:
        msg_in = midi.receive()
        if (isinstance(msg_in, NoteOn) and (msg_in.velocity != 0)):
            # Convert the root note number to a Note object
            root_note = Note.from_number(msg_in.note)
            # Build a major chord with the root note as the tonic
            chord = Chord.build_chord(root_note, 'I', 'major')
            print('Playing major chord with root', root_note, 'from channel', (msg_in.channel + 1))
            # Iterate over the notes in the chord
            for note in chord.notes:
                # Convert the note back to a number
                note_number = note.to_number()
                # Send a NoteOn message for the note
                midi.send(NoteOn(note_number, msg_in.velocity))
        elif (isinstance(msg_in, NoteOff) or (isinstance(msg_in, NoteOn) and (msg_in.velocity == 0))):
            # Convert the root note number to a Note object
            root_note = Note.from_number(msg_in.note)
            # Build a major chord with the root note as the tonic
            chord = Chord.build_chord(root_note, 'I', 'major')
            # Iterate over the notes in the chord
            for note in chord.notes:
                # Convert the note back to a number
                note_number = note.to_number()
                # Send a NoteOff message for the note
                midi.send(NoteOff(note_number, 0))
        elif isinstance(msg_in, MIDIUnknownEvent):
            print('Unknown MIDI event status ', msg_in.status)
        elif (msg_in is not None):
            midi.send(msg_in)
