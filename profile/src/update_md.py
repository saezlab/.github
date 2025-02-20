#!/usr/bin/env python3

#
# Denes Turei <turei.denes@gmail.com>
# Saez Lab 2025
#

import pathlib as pl

import yaml

NCOL = 4

ROOT = pl.Path(__file__).parent.parent
IN_RESOURCES = ROOT / 'src' / 'resources.yaml'
IN_README_MAIN = ROOT / 'src'/ 'README.main.md'
IN_README_FOOT = ROOT / 'src'/ 'README.foot.md'
OUT = ROOT / 'README.md'
LOGOS = ROOT / 'logos'

URL_STEM = 'https://raw.githubusercontent.com/saezlab/.github/main/profile'
URL_ICONS = f'{URL_STEM}/icons'
URL_LOGOS = f'{URL_STEM}/logos'


def main():

    with open(IN_RESOURCES) as fp:

        resources = yaml.load(fp, Loader = yaml.SafeLoader)

    names = resources['order']
    resources = resources['resources']

    with open(IN_README_MAIN) as fp:

        readme = [fp.read() + '\n']

    names = [n for n in names if n in resources]
    names = names + [None] * (len(names) % NCOL)

    for i in range(len(names) // NCOL):

        logos = ['']
        titles = ['']
        links = ['']

        for j in range(NCOL):

            name = names[i * NCOL + j]

            if name:

                res = resources[name]
                l = dict(res['links'])
                main_url = l.get('home', l.get('r', l.get('python')))
                the_logo = f' **{name}** '

                for ext in ('svg', 'png', 'jpeg', 'jpg'):

                    logo = f'{name.lower().replace("+", "plus")}.{ext}'

                    if (LOGOS / logo).exists():

                        the_logo = (
                            f' [<img alt="{name}" src="{URL_LOGOS}/{logo}"'
                            f' width="200"/>]({main_url}) '
                        )
                        break

                logos.append(the_logo)

                titles.append(f' **{name}** {res["main"]} ')

                the_links = []

                for typ, url in res['links']:

                    icon, *pkg = typ.split(':')
                    pkg = f'<sub><sup> {pkg[0]}</sup></sub>' if pkg else ''

                    the_links.append(
                        f'[<img src="{URL_ICONS}/{icon}.svg" '
                        f'height="16">{pkg}]({url})'
                    )

                print(name)

                links.append(' ' + '&nbsp;&nbsp;'.join(the_links) + ' ')

            else:

                logos.append('')
                titles.append('')
                links.append('')

        logos.append('')
        titles.append('')
        links.append('')

        readme.append('|'.join(logos))

        if i == 0:

            readme.append('|' + ' --- |' * NCOL)

        readme.append('|'.join(titles))
        readme.append('|'.join(links))

    with open(IN_README_FOOT) as fp:

        readme.append('\n' + fp.read())

    with open(OUT, 'w') as fp:

        fp.write('\n'.join(readme))


if __name__ == '__main__':

    main()
