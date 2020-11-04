"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

TODO: this is a break out game, you have 3 healths, you need to control
      your mouse to let the paddle move to win the game. if you break 100
      bricks (score = 100), you will win the game.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GLabel
from campy.gui.events.mouse import onmouseclicked

FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3
graphics = BreakoutGraphics()
is_playing = False
hp = NUM_LIVES
dx = graphics.get_vx()
dy = graphics.get_vy()
time = 0   # how long did you play


def main():
    graphics.print_score()
    onmouseclicked(play)
    graphics.window.add(graphics.get_score_label())



def play(mouse):
    global is_playing
    global dx
    global dy
    global hp
    global time
    if not is_playing:
        is_playing = True
        while is_playing:
            graphics.ball.move(dx, dy)
            maybe_object1 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
            maybe_object2 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y)
            maybe_object3 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.height)
            maybe_object4 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y
                                                          + graphics.ball.height)
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.height >= graphics.window.width:
                dx = -dx
            if graphics.ball.y + graphics.ball.height <= 0:
                graphics.ball.move(0,graphics.window.height)
            if maybe_object1 is not None and maybe_object1 is not graphics.get_score_label():
                if maybe_object1 is not graphics.paddle:
                    graphics.add_score(1)
                    graphics.change_score_label()
                    graphics.window.remove(maybe_object1)
                else:
                    graphics.ball.move(0,-10)
                dy = -dy
                graphics.window.add(graphics.get_score_label())
            elif maybe_object2 is not None and maybe_object2 is not graphics.get_score_label():
                if maybe_object2 is not graphics.paddle:
                    graphics.add_score(1)
                    graphics.change_score_label()
                    graphics.window.remove(maybe_object2)
                else:
                    graphics.ball.move(0,-10)
                dy = -dy
                graphics.window.add(graphics.get_score_label())
            elif maybe_object3 is not None and maybe_object3 is not graphics.get_score_label():
                if maybe_object3 is not graphics.paddle:
                    graphics.add_score(1)
                    graphics.change_score_label()
                    graphics.window.remove(maybe_object3)
                else:
                    graphics.ball.move(0,-10)
                dy = -dy
                graphics.window.add(graphics.get_score_label())
            elif maybe_object4 is not None and maybe_object4 is not graphics.get_score_label():
                if maybe_object4 is not graphics.paddle:
                    graphics.add_score(1)
                    graphics.change_score_label()
                    graphics.window.remove(maybe_object4)
                else:
                    graphics.ball.move(0,-10)
                dy = -dy
                graphics.window.add(graphics.get_score_label())
            if graphics.ball.y >= graphics.window.height:
                hp -= 1
                graphics.ball.move(graphics.window.width / 2 - graphics.ball.width / 2 - graphics.ball.x,
                                   -graphics.window.height / 2 - graphics.ball.height / 2)
                is_playing = False
                print(f'Health:{hp}')
            if hp == 0:
                graphics.window.clear()
                lose = GLabel("YOU LOSE!", graphics.window.width/2-160, graphics.window.height/2+20)
                lose.font = '-40'
                graphics.print_score()
                print(f'Playing Times:{time*FRAME_RATE/1000}(s)')
                graphics.window.add(lose)
                break
            if graphics.get_score() == 100:
                graphics.window.clear()
                lose = GLabel("YOU WIN!", graphics.window.width / 2 - 160, graphics.window.height / 2 + 20)
                lose.font = '-40'
                graphics.print_score()
                print(f'Playing Times:{time * FRAME_RATE / 1000}(s)')
                graphics.window.add(lose)
                break
            pause(FRAME_RATE)
            time += 1
        graphics.is_gaming = False


if __name__ == '__main__':
    main()

