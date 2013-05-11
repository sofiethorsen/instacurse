import aalib

def convert(image):
    width, height = image.size
    screen = aalib.AsciiScreen(width=width, height=height/2)
    i = image.convert('L')
    screen.put_image((0, 0), i)
    return screen.render().split('\n')
