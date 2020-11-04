"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    space = (CANVAS_WIDTH-2*GRAPH_MARGIN_SIZE)//len(YEARS)
    x = width + space*year_index
    return x


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    x1 = GRAPH_MARGIN_SIZE
    x2 = CANVAS_WIDTH - GRAPH_MARGIN_SIZE
    y_top = GRAPH_MARGIN_SIZE
    y_bot = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
    canvas.create_line(x1, y_bot, x2, y_bot, width=LINE_WIDTH)
    canvas.create_line(x1, y_top, x2, y_top, width=LINE_WIDTH)
    for i in range(len(YEARS)):
        x = get_x_coordinate(GRAPH_MARGIN_SIZE, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(x+TEXT_DX, y_bot, text=YEARS[i], anchor=tkinter.NW)
    #################################


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid
    # Write your code below this line
    name_list = create_name_list(name_data)
    for j in range(len(lookup_names)):
        for i in range(len(YEARS)):
            x = get_x_coordinate(GRAPH_MARGIN_SIZE, i)
            x_next = get_x_coordinate(GRAPH_MARGIN_SIZE, i + 1)
            lookup_names_with_years = str(YEARS[i]) + lookup_names[j]    # e.g. : '2000Jerry'
            if i != len(YEARS) - 1:
                lookup_names_with_next_years = str(YEARS[i+1]) + lookup_names[j]
            # ----------------------------------------------------------------------
            if lookup_names_with_years in name_list:    # name_list ---> ['1910Jerry', '1910Jerry', '1940Jerry.....]
                y = int(name_data[lookup_names[j]][str(YEARS[i])])
                if lookup_names_with_next_years in name_list:
                    if i != len(YEARS) - 1:
                        y_next = int(name_data[lookup_names[j]][str(YEARS[i + 1])])
                else:
                    y_next = ((CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)-GRAPH_MARGIN_SIZE)/0.56   # it maybe 999.99999...
            else:
                y = ((CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)-GRAPH_MARGIN_SIZE)/0.56   # it maybe 999.99999...
                if lookup_names_with_next_years in name_list:
                    y_next = int(name_data[lookup_names[j]][str(YEARS[i + 1])])
                else:
                    y_next = ((CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)-GRAPH_MARGIN_SIZE)/0.56  # it maybe 999.99999...
            # ----------------------------------------------------------------------
            if i != len(YEARS) - 1:
                canvas.create_line(x, y*0.56+GRAPH_MARGIN_SIZE
                                   , x_next, y_next*0.56+GRAPH_MARGIN_SIZE
                                   , fill=COLORS[j % len(COLORS)]
                                   , width=LINE_WIDTH)
            # ----------------------------------------------------------------------
                if int(y_next+0.1) == 1000:
                    if y > y_next:    # when y < y_next the line will be blocked, and the word will be unclear
                        canvas.create_text(x_next, y_next*0.56+GRAPH_MARGIN_SIZE
                                           , text=f'{lookup_names[j]} : *'
                                           , fill=COLORS[j % len(COLORS)]
                                           , anchor=tkinter.NW)
                    else:
                        canvas.create_text(x_next, y_next * 0.56 + GRAPH_MARGIN_SIZE
                                           , text=f'{lookup_names[j]} : *'
                                           , fill=COLORS[j % len(COLORS)]
                                           , anchor=tkinter.SW)
                    if x != GRAPH_MARGIN_SIZE:
                        continue
                else:
                    if y > y_next:
                        canvas.create_text(x_next, y_next*0.56+GRAPH_MARGIN_SIZE
                                           , text=f'{lookup_names[j]} : {y_next}'
                                           , fill=COLORS[j % len(COLORS)]
                                           , anchor=tkinter.NW)
                    else:
                        canvas.create_text(x_next, y_next * 0.56 + GRAPH_MARGIN_SIZE
                                           , text=f'{lookup_names[j]} : {y_next}'
                                           , fill=COLORS[j % len(COLORS)]
                                           , anchor=tkinter.SW)
                    if x != GRAPH_MARGIN_SIZE:
                        continue
            # ----------------------------------------------------------------------
                if int(y + 0.1) == 1000:
                    canvas.create_text(GRAPH_MARGIN_SIZE, y * 0.56 + GRAPH_MARGIN_SIZE
                                       , text=f'{lookup_names[j]} : *'
                                       , fill=COLORS[j % len(COLORS)]
                                       , anchor=tkinter.SW)
                else:
                    canvas.create_text(GRAPH_MARGIN_SIZE
                                       , y * 0.56 + GRAPH_MARGIN_SIZE
                                       , text=f'{lookup_names[j]} :{y}'
                                       , fill=COLORS[j % len(COLORS)]
                                       , anchor=tkinter.SW)

            # *0.56 meaning : rank have 1000, but the canvas' height have 600 pixels


def create_name_list(name_data):
    """
    :param name_data: dict, the data
    :return: list, create a list from name_data it can help me to detect
             the name's year rank if it out of range(rank 1000)
    """
    l = []
    for key, value in name_data.items():
        year_and_name = ''    # e.g. '2010Eric'
        for i in range(len(YEARS)):
            if str(YEARS[i]) in value:
                year_and_name += str(YEARS[i])
                year_and_name += key
                l.append(year_and_name)
                year_and_name = ''
    return l     # e.g. l == ['1900Eric', '1910Eric', .........]
    #################################


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)
    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
