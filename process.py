#import aalib
import Image
import requests
from cStringIO import StringIO
try:
    import ascii_aalib as ascii
except:
    import ascii_py as ascii

url = 'http://carmenza.spotlife.se/files/2012/11/instagram-logo1.jpg'

def get_image(url):
    r = requests.get(url)
    return Image.open(StringIO(r.content))

def render(image, width, height):
    output = ascii.convert(image.resize((width, height)))
    for line in output:
        print line

i = get_image(url)
render(i, 80, 40)
