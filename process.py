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
    image = Image.open(StringIO(r.content))
    data = ascii.convert(image.resize((width, height)))
    return CurseImage(data)
