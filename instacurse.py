import sys

import curses

import gevent

from image import CurseImage

def main():
    Application().run()

class Application(object):
    def run(self):
        try:
            # TODO: Provide better logging mechanism
            sys.stdout = open('log.txt', 'a', 0)
            curses.wrapper(self._run)
        finally:
            sys.stdout = sys.__stdout__

    def _run(self, screen):
        page = WelcomePage(screen)

        self._main_loop(page)

    def _main_loop(self, page):
        while page:
            page = page.run()

class Page(object):
    def __init__(self, parent):
        self.screen = parent.screen

class WelcomePage(Page):
    def __init__(self, screen):
        self.screen = screen

    def run(self):
        screen = self.screen

        logo = CurseImage.from_file('extras/logo.txt')

        height, width = screen.getmaxyx()
        x = width / 2 - logo.width / 2
        start_y = height / 2 - logo.height / 2

        for y, row in enumerate(logo.data, start=start_y):
            screen.addstr(y, x, row)

        screen.refresh()

        while True:
            c = _getch(self.screen)

def _getch(screen):
    gevent.socket.wait_read(sys.stdin.fileno())
    return screen.getch()

if __name__ == '__main__':
    main()


