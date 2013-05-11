import curses

pair_number = 0

class CurseImage(object):
    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r') as file:
            return CurseImage(list(file))

    @classmethod
    def from_image(cls, image):
        pass

    def __init__(self, data, color=None):
        self.data = data
        self.color = color
        self.width = max((len(row) for row in data))
        self.height = len(data)

    def draw(self, screen, offset_y, offset_x):
        height, width = screen.getmaxyx()
        for y, row in enumerate(self.data, start=offset_y):
            if y >= height - 1 or y < 0:
                continue

            if not self.color:
                screen.addstr(y, offset_x, row)
            else:
                for x, ch in enumerate(row, start=offset_x):
                    attr = curses.color_pair(self.color[y - offset_y][x - offset_x])
                    screen.addch(y, x, ch, attr)
