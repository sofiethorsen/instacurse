from itertools import product

import curses

iterations = int(256 / 1.5)

def init(screen):
    count = 10
    for r, g, b in product(range(0, 1000, iterations), repeat=3):
        #print r, g, b
        curses.init_color(count, r, g, b)
        curses.init_pair(count, count, 0)
        count += 1

    #for r in range(1000):
    #    for g in range(1000)
