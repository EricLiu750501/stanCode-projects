"""
File: draw_line
Name:Eric Liu
-------------------------
TODO: The program can draw a line. If you want to create a line,
      you must click twice on the different two site, the first
      time, the program will make a small circle mark; the second
      time, the program will make a line and remove the mark.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
count = 0
window = GWindow()
OVAL_SIZE = 10
oval = GOval(OVAL_SIZE,OVAL_SIZE)
one_st_x = 0
one_st_y = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(make_line)


def make_line(mouse):
    """
     the code can make a line
    """
    global count
    global one_st_x
    global one_st_y
    count += 1
    if count % 2 == 1:
        window.add(oval, mouse.x - OVAL_SIZE // 2, mouse.y - OVAL_SIZE // 2)
        one_st_x = mouse.x
        one_st_y = mouse.y
    else:
        window.remove(oval)
        line = GLine(one_st_x, one_st_y, mouse.x, mouse.y)
        window.add(line)


if __name__ == "__main__":
    main()
