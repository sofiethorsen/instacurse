class CurseImage(object):
    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r') as file:
            return CurseImage(list(file))

    def __init__(self, data):
        self.data = data
        self.width = max((len(row) for row in data))
        self.height = len(data)
