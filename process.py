import Image
import requests
from cStringIO import StringIO

from image import CurseImage

url = 'http://carmenza.spotlife.se/files/2012/11/instagram-logo1.jpg'


def get_image(url, width, height):
    url = 'https://fbcdn-sphotos-d-a.akamaihd.net/hphotos-ak-prn1/11418_10151419680844375_440985203_n.jpg'
    r = requests.get(url)
    image = Image.open(StringIO(r.content)).resize((width, height))
    return CurseImage.from_image(image)
