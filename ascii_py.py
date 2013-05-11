'''
ASCII Art maker
Creates an ascii art image from an arbitrary image
Created on 7 Sep 2009

@author: Steven Kay
'''

from PIL import Image
import random
from bisect import bisect

# greyscale.. the following strings represent
# 7 tonal ranges, from lighter to darker.
# for a given pixel tonal level, choose a character
# at random from that range.

greyscale = [
    " ",
    ".",
    ".,-",
    "_ivc=!/|\\~",
    "gjez2]/(YL)t[+T7Vf",
    "mdK4ZGbNDXY5P*Q",
    "W8KMA",
    "#%$"
]

# using the bisect class to put luminosity values
# in various ranges.
# these are the luminosity cut-off points for each
# of the 7 tonal levels. At the moment, these are 7 bands
# of even width, but they could be changed to boost
# contrast or change gamma, for example.

zonebounds = [36, 72, 108, 144, 180, 216, 252]


def convert(image):
    # open image and resize
    # experiment with aspect ratios according to font

    # convert to mono
    image = image.convert("L")

    # now, work our way over the pixels
    # build up str

    pixels = image.load()

    output = []
    for y in range(0,image.size[1]):
        line = ''

        for x in range(0,image.size[0]):
            lum = 255 - pixels[x, y]
            row = bisect(zonebounds, lum)
            possibles = greyscale[row]
            line += possibles[random.randint(0, len(possibles) - 1)]
        output.append(line)

    return output
