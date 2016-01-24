from visualisation import draw_map
from visualisation import input_for_david as inp


def make_map(tobjects):

    data = inp.generate_lists_for_map(tobjects)
    draw_map.draw_map(data[0], data[1], data[2])
    return 0
