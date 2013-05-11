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
        self._main_loop(screen)

    def _main_loop(self, screen):
        while True:
            c = self._getch(screen)


    def _getch(self, screen):
        gevent.socket.wait_read(sys.stdin.fileno())
        return screen.getch()

if __name__ == '__main__':
    main()
