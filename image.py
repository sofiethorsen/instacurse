class CurseImage(object):
    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r') as file:
            return CurseImage(list(file))

    def __init__(self, data):
        self.data = data
        self.width = max((len(row) for row in data))
        self.height = len(data)

    def draw(self, screen, y, x):
        height, width = screen.getmaxyx()
        for y, row in enumerate(self.data, start=y):
            if y >= height - 1:
                break

            screen.addstr(y, x, row)
