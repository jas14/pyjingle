#!/usr/bin/env python
import argparse
import re
from notes import Note
# from subprocess import call


def main():
    parser = argparse.ArgumentParser(description='Play a jingle')
    parser.add_argument('jingle', help='jingle file')
    parser.add_argument('--speed', type=int,
                        help='1-unit note speed in milliseconds')

    args = parser.parse_args()
    player = Note()

    if args.speed:
        player.set_speed(args.speed)

    with open(args.jingle) as jingle_file:
        ws = re.compile(r'[ \t]+')
        for line in jingle_file.xreadlines():
            if line.strip() == '':
                continue

            for note in ws.split(line.strip()):
                player.play(note)

if __name__ == "__main__":
    main()
