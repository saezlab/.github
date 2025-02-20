#!/usr/bin/env python3

#
# Denes Turei <turei.denes@gmail.com>
# Saez Lab 2025
#

import pathlib as pl
import re

import yaml

ROOT = pl.Path(__file__).parent.parent
SOURCE = ROOT / 'snapshot' / 'README.md'
OUT = ROOT / 'src' / 'resources.yaml'
REMAIN = re.compile(r'\*\*([\w\+]+)\*\* ([-\+,\w\s]+)')
RELINK = re.compile(
    r'([-\w]+)\.svg.+?>'
    r'(?:<sub><sup> (\w+)</sup></sub>)?'
    r'\]\((http.+?)\)'
)


def main():

    lines = []
    out = {}

    with open(SOURCE) as fp:

        for line in fp:

            if line.startswith('|'):

                line = line.split('|')[1:-1]
                line = [x.strip() for x in line]

                if line[0].startswith('---'):

                    continue

                lines.append(line)

    for i in range(len(lines) // 3):

        for main, links in zip(lines[i * 3 + 1], lines[i * 3 + 2]):

            if m := REMAIN.match(main):

                name, desc = m.groups()

            else:

                continue

            out[name] = {
                'main': desc,
                'links': [
                    [
                        ':'.join(l[0:2]) if l[1] else l[0],
                        l[2]
                    ]
                    for l in RELINK.findall(links)],
            }

    out = {
        'order': list(out.keys()),
        'resources': out,
    }

    with open(OUT, 'w') as fp:

        yaml.dump(out, fp, sort_keys = False)


if __name__ == '__main__':

    main()
