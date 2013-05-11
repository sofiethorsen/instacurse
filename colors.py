from itertools import product

import curses

_colors = {}

def init():
    pair = 0

    for r, g, b in product(range(0b111 + 1), range(0b111 + 1), range(0b11 + 1)):
        if pair + 8 >= 255:
            break

        pair += 1
        curses.init_color(pair + 8, int(r / float(0b111) * 1000), int(g / float(0b111) * 1000), int(b / float(0b11) * 1000))
        curses.init_pair(pair, pair + 8, 0)

        _colors[(r, g, b)] = pair

    return

def pair(r, g, b):
    return _colors.get((r >> 5, g >> 5, b >> 6), 0)
