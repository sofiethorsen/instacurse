from itertools import product

import Image
import requests
from cStringIO import StringIO
try:
    import ascii_aalib as ascii
except:
    import ascii_py as ascii

from image import CurseImage
import colors

url = 'http://carmenza.spotlife.se/files/2012/11/instagram-logo1.jpg'


def get_image(url, width, height):
    url = 'http://www.bluesky-web.com/images2012/color.jpg'
    r = requests.get(url)
    image = Image.open(StringIO(r.content)).resize((width, height))
    data = ascii.convert(image)
    color = get_color(image)
    return CurseImage(data, color)

def get_color(image):
    width, height = image.size
    pixels = image.load()
    color = [[0 for x in range(width + 1)] for y in range(height + 1)]
    for y, x in product(range(height), range(width)):
        r, g, b = pixels[x, y]
        color[y][x] = colors.pair(r, g, b)
    return color
