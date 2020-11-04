"""
File: sierpinski.py
Name: 
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause
from  campy.graphics.gobjects import GPolygon
# Constants
ORDER = 3                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	the program can make the sierpinski_triangle, click run and take a look at it !
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
											line1
											-----------
											 \       /
											  \     /
								line2		   \   /	line3
												\ /
	:param order: int, Controls the order of Sierpinski Triangle
	:param length: int, The length of order 1 Sierpinski Triangle
	:param upper_left_x: int, The upper left x coordinate of order 1 Sierpinski Triangle
	:param upper_left_y: int, The upper left y coordinate of order 1 Sierpinski Triangle
	:return:
	"""
	if order == 0:
		pass
	else:
		# line1 = GLine(upper_left_x, upper_left_y, upper_left_x + length, upper_left_y)
		# line2 = GLine(upper_left_x, upper_left_y, upper_left_x + 0.5*length, upper_left_y + (3**0.5)/2*length)
		# line3 = GLine(upper_left_x + length, upper_left_y, upper_left_x + 0.5*length, upper_left_y + (3**0.5)/2*length)
		# window.add(line1)
		# window.add(line2)
		# window.add(line3)

		# if you want to draw the triangle, you can use it
		# ----------------------------------------------------------------
		triangle = GPolygon()
		triangle.add_vertex((upper_left_x, upper_left_y))
		triangle.add_vertex((upper_left_x + length, upper_left_y))
		triangle.add_vertex((upper_left_x + 0.5*length, upper_left_y + (3**0.5)/2*length))
		# draw it from the line!
		# e.g.
		triangle.filled = True
		if order % 3 == 0:
			triangle.fill_color = 'blue'
		elif order % 3 == 1:
			triangle.fill_color = 'magenta'
		else:
			triangle.fill_color = 'pink'

		window.add(triangle)
		# ----------------------------------------------------------------


		# make the upper left triangle
		sierpinski_triangle(order-1, length/2, upper_left_x, upper_left_y)

		# make the upper right triangle
		sierpinski_triangle(order-1, length/2, upper_left_x + length/2, upper_left_y)

		# make the lower triangle
		sierpinski_triangle(order-1, length/2, upper_left_x + 0.25*length, upper_left_y + (3**0.5)/2*(length/2))


if __name__ == '__main__':
	main()