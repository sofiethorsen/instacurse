import curses

pair_number = 0

class CurseImage(object):
    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r') as file:
            return CurseImage(list(file))

    def __init__(self, data, color=None):
        self.data = data
        self.color = color
        self.width = max((len(row) for row in data))
        self.height = len(data)

    def draw(self, screen, offset_y, offset_x):
        height, width = screen.getmaxyx()
        for y, row in enumerate(self.data, start=offset_y):
            if y >= height - 1:
                break

            if not self.color:
                screen.addstr(y, offset_x, row)
            else:
                for x, ch in enumerate(row, start=offset_x):
                    attr = curses.color_pair(self.color[y][x] + 10)
                    screen.addch(y, x, ch, attr)
