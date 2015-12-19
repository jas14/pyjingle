from subprocess import call
import re
from time import sleep


class Note:
    _notes = {
        'A': 440,  # a4
        'A#': 466,
        'Bb': 466,
        'B': 493,
        'C': 523,  # c5
        'C#': 554,
        'Db': 554,
        'D': 587,
        'D#': 622,
        'Eb': 622,
        'E': 659,
        'F': 698,
        'F#': 740,
        'Gb': 740,
        'G': 783,
        'G#': 831,
        'Ab': 831
    }

    def __init__(self):
        self.note = re.compile(r'([0-9]+)?([a-gA-Gr][#b]?)([1-9])?')
        self.tempo = 250

    def toHz(self, string):
        if string.upper() in self._notes:
            return self._notes[string]
        return None

    def setTempo(self, millis):
        self.tempo = millis

    def play(self, note_str):
        low_pitches = ['A', 'A#', 'Bb', 'B']
        note_str = note_str.strip()
        if note_str == "":
            return

        note = self.note.match(note_str.strip())
        duration = note.group(1)
        if duration is None:
            duration = 1
        else:
            duration = int(duration)

        pitch = note.group(2)
        pitch = pitch[0].upper() + pitch[1:]
        if pitch not in self._notes and pitch != 'R':
            raise Exception("Bad note {0}".format(note_str))

        octave = note.group(3)
        if octave is None:
            octave = 0
        else:
            octave = int(octave) - (4 if pitch in low_pitches else 5)

        if pitch != 'R':
            freq = self._notes[pitch] * pow(2, octave)
        duration_millis = duration * self.tempo

        if pitch == 'R':  # rest
            sleep(float(duration_millis) / 1000)
        else:
            call(['beep', '-f {0}'.format(freq),
                  '-l {0}'.format(duration_millis)])
