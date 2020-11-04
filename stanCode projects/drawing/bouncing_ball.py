"""
File: bouncing_ball
Name: Erc Liu
-------------------------
TODO: This is a program that simulate the reality world's gravity.
      The ball on the window will drop when you click and bounce if
      drop on the ground, like real world. If the ball disappear from
      the window the program will reset , start form the the beginning
      , and it will repeat 3 times.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
is_moving = False
click_time = 3


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    window.add(ball, x=START_X, y=START_Y)
    onmouseclicked(bouncing)


def bouncing(mouse):
    """
    when you click, the code will be launched.
    this simulate the world gravity.
    """
    global is_moving
    global click_time
    if not is_moving and click_time > 0:
        click_time -= 1
        is_moving = True
        window.add(ball, x=START_X, y=START_Y)
        s = 0
        vy = GRAVITY
        vx = VX
        while True:
            ball.move(vx, vy)
            if ball.x + ball.width >= window.width:
                reset()
                break
            vy += GRAVITY
            if ball.y + ball.height >= window.height:
                vy = -REDUCE * vy
            pause(DELAY)
            s += DELAY
        is_moving = False


def reset():
    """
    if the ball disappear from the window, it will be launched.
    this reset the ball to the beginning
    """
    global ball
    window.remove(ball)
    window.add(ball, x=START_X, y=START_Y)


if __name__ == "__main__":
    main()
