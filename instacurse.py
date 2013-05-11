import sys

import curses
import colors

import gevent
import gevent.monkey

from image import CurseImage
import instagram
import process

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

        colors.init(screen)

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

        self.animate_logo(screen, logo)

        _getch(screen)

        return LoadingPage(ImagesPage, instagram.popular)

    def animate_logo(self, screen, logo):
        height, width = screen.getmaxyx()

        x = width / 2 - logo.width / 2
        y_center =  height / 2 - logo.height / 2 - 1
        y_start = 0

        while y_start < y_center:
            screen.clear()

            logo.draw(screen, y_start, x)

            y_start += 1
            screen.refresh()
            gevent.sleep(seconds=0.05)

        addstr_centered(screen, y_center + logo.height + 1, "PRESS ANY KEY")

        screen.refresh()


class ImagesPage(Page):
    def __init__(self, images):
        self.images = images

    def run(self, screen):
        #gevent.spawn(self._fetch_images).join()

        height, width = screen.getmaxyx()
        image = process.get_image(self.images[0].low_res['url'], width, height)
        image.draw(screen, 0, 0)
        screen.refresh()

        while True:
            c = _getch(screen)

class LoadingPage(Page):
    def __init__(self, page_cls, fn):
        self.page_cls = page_cls
        self.fn = fn
        self.running = True

    def run(self, screen):
        gevent.spawn(self.fn).link(self._load_completed)

        logo = CurseImage.from_file('extras/loading.txt')

        height, width = screen.getmaxyx()
        x_center = width / 2 - logo.width / 2
        y_center = height / 2 - logo.height / 2 - 1

        while self.running:
            for row in range(len(logo.data)):
                if row % 2 == 0:
                    for column in range(len(logo.data[row])):
                        screen.addch(y_center, x_center + column, ' ')
                        screen.refresh()
                        gevent.sleep(seconds=0.05)

                        for y, row in enumerate(logo.data, start=y_center):
                            screen.addstr(y, x_center, row)
                else:
                    for column in reversed(range(len(logo.data[row]))):
                        screen.addch(y_center + 1, x_center + column, ' ')
                        screen.refresh()
                        gevent.sleep(seconds=0.05)

                        for y, row in enumerate(logo.data, start=y_center):
                            screen.addstr(y, x_center, row)

        return self.page_cls(self.arg)

    def _load_completed(self, greenlet):
        self.arg = greenlet.value
        self.running = False

def addstr_centered(screen, y, text):
    height, width = screen.getmaxyx()
    x = width / 2 - len(text) / 2
    screen.addstr(y, x, text)

def _getch(screen):
    gevent.socket.wait_read(sys.stdin.fileno())
    return screen.getch()

if __name__ == '__main__':
    main()
