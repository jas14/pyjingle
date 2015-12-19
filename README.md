# pyjingle

Pyjingle reads .jingle files and plays them using [beep](https://github.com/johnath/beep).

## Usage
`./pyjingle.py [--speed SPEED] jingle_file`

* `--speed SPEED` specifies the duration of the unit note in milliseconds

## Jingle Format
.jingle files are made up of whitespace-separated _notes_. Each note is formatted like so: `[speed]pitch[octave]`,
where:

* `[speed]` is an optional ratio to the unit note (e.g. if the quarter note is the unit note, 0.25 is a sixteenth note)
* `pitch` is either:
    * a note `a-g` with or without a sharp `#` or flat `b` (case-insensitive). There is no `B#`, `Cb`, `E#`, or `Fb`.
    * a rest `r` (in which case `octave` is ignored)
* `octave` is an integer indicating the octave of the note. `A4` 440 Hz.

To comment out a line in a jingle file, make its first character a `%`.

See the `jingles` folder for examples.
