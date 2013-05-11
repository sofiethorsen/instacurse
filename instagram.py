import requests
import string

_BASE_URL = 'https://api.instagram.com/v1'
_CLIENT_ID = 'e55279a2d0124296af2423a09d83c2c6'

def request_images(path):
    url = _BASE_URL + path
    return _parse_result(requests.get(url, params = {'client_id':_CLIENT_ID}).json())

def _parse_result(json):
    pictures = []
    for entry in json['data']:
        user = entry['user']
        info = entry['caption']
        images = entry['images']
        pictures.append(InstagramPicture(user, info, images))
    return pictures

class InstagramPicture(object):
    def __init__(self, user, info, images):
        self.username = user['username']
        self.images = images
        self.text = ''

        if info:
            text = filter(lambda x: x in string.printable, info['text']).replace('\n', ' ')
            self.text = text

        for key, value in images.iteritems():
            if key == 'low_resolution':
                self.low_res = value
            elif key == 'thumbnail':
                self.thumbnail = value
            elif key == 'standard_resolution':
                self.standard_res = value

    def __repr__(self):
        return '<{} {}>'.format(self.username, self.text[:10])
