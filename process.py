import Image
import requests
from cStringIO import StringIO

from image import CurseImage

url = 'http://carmenza.spotlife.se/files/2012/11/instagram-logo1.jpg'

def get_image(url, width, height):
    r = requests.get(url)
    image = Image.open(StringIO(r.content)).resize((width, height))
    return CurseImage.from_image(image)
