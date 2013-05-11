import sys

import curses

import gevent

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
        page = LoginPage(screen)

        self._main_loop(page)

    def _main_loop(self, page):
        while page:
            page = page.run()

class Page(object):
    def __init__(self, parent):
        self.screen = parent.screen

class LoginPage(Page):
    def __init__(self, screen):
        self.screen = screen

    def run(self):
        while True:
            c = _getch(self.screen)

def _getch(screen):
    gevent.socket.wait_read(sys.stdin.fileno())
    return screen.getch()

if __name__ == '__main__':
    main()


