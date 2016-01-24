from . import draw_map
from . import input_for_david as inp


def make_map(tobjects):

    data = inp.generate_lists_for_map(tobjects)
    numbers = [2, 4, 6, 8, 10]
    draw_map.draw_map(data[1], data[0], data[2], numbers)
    return 0
