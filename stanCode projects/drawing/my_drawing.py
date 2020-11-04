"""
File: my_drawing
Name: Eric Liu
----------------------
TODO: The program will make a title and a dna sign.
      the dna sign is make from 'import math' to make
      two sine lines and combine to a dna sign.
"""

from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.graphics.gwindow import GWindow
import math
W_SIZE = 750
window = GWindow(W_SIZE,W_SIZE * 4 // 9, title='Similarity.py sign')
OVAL_SIZE = 5
DNA_LEN = 812  # cooperate with the W_SITE
DNA_HIGH = 50
DNA_DENSITY = 0.04    # the bigger, the denser   if you have Intensive phobia, please careful!!!


def main():
    """
    this program will make a similarity.py question sign on the window.
    I hope it will put on SC001~
    """
    make_dna()
    make_title()


def make_title():
    """
    this code can make a title on the window
    """
    title = GLabel('Similarity.py')
    title.font = '-70'
    window.add(title, 50, 150)


def make_dna():
    """
    this code can make a dna sign on the window (with math.sin())
    """
    for i in range(1, DNA_LEN, 1):
        i *= 0.5
        o1_y = W_SIZE // 3 + DNA_HIGH * math.sin(DNA_DENSITY * i - 9)
        o2_y = W_SIZE // 3 - DNA_HIGH * math.sin(DNA_DENSITY * i - 9)
        o3_y = W_SIZE // 3 + DNA_HIGH * math.sin(DNA_DENSITY * i)
        o4_y = W_SIZE // 3 - DNA_HIGH * math.sin(DNA_DENSITY * i)
        oval1 = GOval(OVAL_SIZE, OVAL_SIZE, x=W_SIZE // 2 + i, y=o1_y)
        oval2 = GOval(OVAL_SIZE, OVAL_SIZE, x=W_SIZE // 2 - i, y=o2_y)
        oval3 = GOval(OVAL_SIZE, OVAL_SIZE, x=W_SIZE // 2 + i, y=o3_y)
        oval4 = GOval(OVAL_SIZE, OVAL_SIZE, x=W_SIZE // 2 - i, y=o4_y)
        oval1.filled = True
        oval2.filled = True
        oval3.filled = True
        oval4.filled = True
        oval1.color = 'red'
        oval2.color = 'red'
        oval3.color = 'green'
        oval4.color = 'green'
        rect_len = DNA_HIGH * math.sin(DNA_DENSITY * i - 9)-DNA_HIGH * math.sin(DNA_DENSITY * i)
        rect2 = GRect(OVAL_SIZE//2, rect_len, x=oval2.x, y=oval2.y)
        rect3 = GRect(OVAL_SIZE//2,rect_len , x=oval3.x, y=oval3.y)
        rect2.color = 'darkgreen'
        rect3.color = 'darkgreen'
        rect2.filled = True
        rect3.filled = True
        if rect2.x % 25 == 0 :
            window.add(rect2)
        if rect3.x % 25 == 0:
            window.add(rect3)
        window.add(oval1)
        window.add(oval2)
        window.add(oval3)
        window.add(oval4)


if __name__ == '__main__':
    main()
