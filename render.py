import process

class Renderer(object):
    def __init__(self, screen, offset, spacing, images):
        self.screen = screen
        self.images = images
        self.offset = offset
        self.spacing = spacing
        y, x = self.screen.getmaxyx()

        self.width = x - self.spacing
        self.height = x/2

    def render(self):
        #for image in self.images:
        ascii_image = process.get_image(self.images[0].low_res['url'], self.width, self.height)
        self.draw(self.screen, ascii_image, self.images[0])

    def _display_text(self, screen, ascii_image, image):
        y = self.offset + ascii_image.height
        x = self.spacing/2
        #screen.addstr(y, x, image.text)

    def draw(self, screen, ascii_image, image):
        screen.erase()
        ascii_image.draw(screen, self.offset, self.spacing/2)
        self._display_text(screen, ascii_image, image)
        screen.refresh()