from image import CurseImage
import gevent

def loading_animation(screen):
    logo = CurseImage.from_file('extras/loading.txt')

    height, width = screen.getmaxyx()
    x_center = width / 2 - logo.width / 2
    y_center =  height / 2 - logo.height / 2 - 1

    while True:
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