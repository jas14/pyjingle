# pyjingle

Pyjingle reads .jingle files and plays them using [beep](https://github.com/johnath/beep).

## Usage
`./pyjingle.py [--rate RATE] jingle_file`

* `--rate RATE` specifies the factor by which to increase the tempo.

## Jingle Format
.jingle files are made up of lines with either a _command_, a list of whitespace-separated _notes_, or a comment. Each note is formatted like so: `[speed]pitch[octave]`,
where:

* `[speed]` is an optional ratio to the unit note (e.g. if the quarter note is the unit note, 0.25 is a sixteenth note)
* `pitch` is either:
    * a note `a-g` with or without a sharp `#` or flat `b` (case-insensitive). There is no `B#`, `Cb`, `E#`, or `Fb`.
    * a rest `r` (in which case `octave` is ignored)
* `octave` is an integer indicating the octave of the note. `A4` 440 Hz.

To comment out a line in a jingle file, make its first character a `%`.

_Command_ lines have the following format: `* name value` where `name` is the setting name and `value` is the new value of the setting. Currently supported commands are:

* `speed <ms>` changes the unit note duration to `<ms>` milliseconds unless the `--speed` command-line interface was specified. Until specified in the file, the unit note duration is 250ms.

See the `jingles` folder for examples.
