import time
import board
import touchio
import usb_midi

from adafruit_midi import MIDI
from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff



pins = [
    board.IO13,
    board.IO12,
    board.IO11,
    board.IO10,
    board.IO9,
    board.IO8,
    board.IO7
]

sensor = [
    touchio.TouchIn(pin) for pin in pins
]

notes = [60, 62, 64, 65, 67, 69, 71] #C, D, E, F, G, A, B

midi = MIDI(
    midi_out=usb_midi.ports[1],
    out_channel=0
)


while True:
    for i, key in enumerate(sensor):
        touched = key.value

        if touched:
            midi.send(NoteOn(notes[i], 100))
        elif not touched:
            midi.send(NoteOff(notes[i], 0))

        time.sleep(0.01)