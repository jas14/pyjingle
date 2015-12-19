#!/usr/bin/env python
import argparse
import re
from notes import Note
# from subprocess import call


def main():
    parser = argparse.ArgumentParser(description='Play a jingle')
    parser.add_argument('jingle', help='jingle file')
    parser.add_argument('--rate', type=float,
                        help='Factor by which to increase tempo')
    parser.add_argument('--shift', type=int,
                        help='Number of octaves to shift pitches')

    args = parser.parse_args()
    player = Note()

    if args.rate:
        player.set_rate(args.rate)

    if args.shift:
        player.set_shift(args.shift)

    line_no = 0
    with open(args.jingle) as jingle_file:
        ws = re.compile(r'[ \t]+')
        for line in jingle_file.xreadlines():
            line_no += 1
            line = line.strip()
            if line == '' or line[0] == '%':
                # ignore blank lines and comments
                continue
            elif line[0] == '*':
                # setting line
                key, val = line[1:].strip().split(' ')
                if key == 'speed':
                    # use suggested speed
                    player.set_speed(int(val))
                else:
                    print ("Parse error: Unrecognized setting \"{0}\" "
                           "on line {1}".format(key, line_no))
                    return
                continue

            for note in ws.split(line):
                player.play(note)

if __name__ == "__main__":
    main()
