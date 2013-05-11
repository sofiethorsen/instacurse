import sys
import math

import curses
import colors

import gevent
import gevent.monkey

from image import CurseImage
from render import Renderer

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
            sys.stderr = open('log.txt', 'a', 0)
            curses.wrapper(self._run)
        finally:
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__

    def _run(self, screen):
        curses.curs_set(0)
        curses.mousemask(1)

        screen.nodelay(1)

        colors.init()

        page = WelcomePage()

        self._main_loop(screen, page)

    def _main_loop(self, screen, page):
        while page:
            screen.erase()
            screen.refresh()
            page = page.run(screen)

class Page(object):
    pass

class WelcomePage(Page):
    def run(self, screen):
        logo = CurseImage.from_file('extras/logo.txt')

        self.animate_logo(screen, logo)

        _getch(screen)

        return LoadingPage(ImagesPage())

    def animate_logo(self, screen, logo):
        height, width = screen.getmaxyx()

        x = width / 2 - logo.width / 2
        y_center = height / 2 - logo.height / 2 - 1
        y_start = 0

        for y in range(y_start, y_center):
            screen.erase()

            logo.draw(screen, y, x)

            screen.refresh()
            gevent.sleep(seconds=0.05)

        addstr_centered(screen, y_center + logo.height + 1, "PRESS ANY KEY")

        screen.refresh()

class AsyncPage(Page):
    def fetch(self, screen):
        pass

class ImagesPage(AsyncPage):
    def __init__(self):
        self.current_image = 0
        self.spacing = 10

    def fetch(self, screen):
        self.images = instagram.popular()

    def run(self, screen):
        if self.current_image >= len(self.images):
            # Load more images
            return LoadingPage(ImagesPage())
        else:
            image = self.images[self.current_image]
            self.current_image += 1
            return LoadingPage(ImagePage(image, self))

class ImagePage(AsyncPage):
    def __init__(self, image, next_page):
        self.image = image
        self.next_page = next_page
        self.spacing = 10

    def fetch(self, screen):
        height, width = screen.getmaxyx()
        width -= self.spacing
        height = width / 2

        self.ascii_image = process.get_image(self.image.low_res['url'], width, height)

    def run(self, screen):
        self.display_image(screen, self.ascii_image, self.image)

        _getch(screen)
        return self.next_page

    def display_image(self, screen, ascii_image, image):
        height, width = screen.getmaxyx()
        width -= self.spacing
        height = width / 2

        ascii_image.draw(screen, 0, self.spacing / 2)
        #self.display_text(screen, ascii_image.height, image)
        screen.refresh()

    def display_text(self, screen, offset_y, image):
        screen_height, screen_width = screen.getmaxyx()
        width = screen_width - self.spacing
        x = self.spacing / 2
        y = offset_y
        text = image.text
        while True:
            part = text[:width]
            text = text[width:]
            if y >= screen_height or not part:
                break
            screen.addstr(y, x, part)
            y += 1

class LoadingPage(Page):
    def __init__(self, page):
        self.page = page
        self.running = True

    def run(self, screen):
        self.screen = screen
        gevent.spawn(self.page.fetch, screen).link(self._load_completed)

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

        return self.page

    def _load_completed(self, greenlet):
        if not greenlet.exception:
            self.running = False
        else:
            gevent.spawn(self.page.fetch, self.screen).link(self._load_completed)

def addstr_centered(screen, y, text):
    height, width = screen.getmaxyx()
    x = width / 2 - len(text) / 2
    screen.addstr(y, x, text)

def _getch(screen):
    gevent.socket.wait_read(sys.stdin.fileno())
    return screen.getch()

if __name__ == '__main__':
    main()
