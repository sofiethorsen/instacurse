from itertools import product

import Image
import requests
from cStringIO import StringIO
try:
    import ascii_aalib as ascii
except:
    import ascii_py as ascii

from image import CurseImage

url = 'http://carmenza.spotlife.se/files/2012/11/instagram-logo1.jpg'


def get_image(url, width, height):
    r = requests.get(url)
    image = Image.open(StringIO(r.content)).resize((width, height))
    data = ascii.convert(image)
    color = get_color(image)
    return CurseImage(data, color)

def get_color(image):
    image = image.convert('P', palette=Image.ADAPTIVE, colors=256)
    width, height = image.size
    pixels = image.load()
    color = [[0 for x in range(width + 1)] for y in range(height + 1)]
    for y, x in product(range(height), range(width)):
        #print pixels[x, y]
        color[y][x] = pixels[x, y]
    #print r, g, b
    return color
