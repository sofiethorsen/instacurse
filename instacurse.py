import sys

import curses

import gevent
import gevent.monkey

from image import CurseImage

gevent.monkey.patch_all(thread=False)

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
        curses.curs_set(0)
        curses.mousemask(1)

        screen.nodelay(1)

        print curses.can_change_color()

        page = WelcomePage()

        self._main_loop(screen, page)

    def _main_loop(self, screen, page):
        while page:
            screen.clear()
            screen.refresh()
            page = page.run(screen)

class Page(object):
    pass

class WelcomePage(Page):
    def run(self, screen):
        logo = CurseImage.from_file('extras/logo.txt')

        height, width = screen.getmaxyx()
        x = width / 2 - logo.width / 2
        start_y = height / 2 - logo.height / 2 - 1

        for y, row in enumerate(logo.data, start=start_y):
            screen.addstr(y, x, row)

        addstr_centered(screen, start_y + logo.height + 1, "PRESS ANY KEY")

        screen.refresh()

        _getch(screen)

        return PopularPage()

class PopularPage(Page):
    def run(self, screen):

        while True:
            c = _getch(screen)


def addstr_centered(screen, y, text):
    height, width = screen.getmaxyx()
    x = width / 2 - len(text) / 2
    screen.addstr(y, x, text)

def _getch(screen):
    gevent.socket.wait_read(sys.stdin.fileno())
    return screen.getch()

if __name__ == '__main__':
    main()
