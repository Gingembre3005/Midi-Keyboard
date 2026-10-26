import time
import board
import touchio
import usb_midi
import digitalio

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

octave = 0

upKey = digitalio.DigitalInOut(board.IO4)
upKey.direction = digitalio.Direction.INPUT
upKey.pull = digitalio.Pull.UP

downKey = digitalio.DigitalInOut(board.IO5)
downKey.direction = digitalio.Direction.INPUT
downKey.pull = digitalio.Pull.UP


midi = MIDI(
    midi_out=usb_midi.ports[1],
    out_channel=0
)


while True:
    for i, key in enumerate(sensor):
        touched = key.value

        upKey_pressed = not upKey.value
        downKey_pressed = not downKey.value

        if upKey_pressed:
            octave += 1

        if downKey_pressed:
            octave -= 1

        if touched:
            midi.send(NoteOn(notes[i] + octave * 12, 100))
        elif not touched:
            midi.send(NoteOff(notes[i] + octave * 12, 0))

        time.sleep(0.01)
