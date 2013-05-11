import aalib
import Image
import requests
from cStringIO import StringIO

url = 'http://carmenza.spotlife.se/files/2012/11/instagram-logo1.jpg'

def get_image(url):
    r = requests.get(url)
    return Image.open(StringIO(r.content))

def render(image, size):
    """
    size should be a tuple of (x,y)
    """
    screen = aalib.AsciiScreen(width=size[0], height=size[1])
    i = image.convert('L').resize(size)
    screen.put_image((0, 0), i)
    print screen.render()

i = get_image(url)
render(i, (80, 40))
