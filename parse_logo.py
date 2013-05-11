logo = open('extras/logo.txt', 'r')
_characters = []

for line in logo:
    _characters.append(line)

def get_characters():
    return _characters