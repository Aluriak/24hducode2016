from draw_map import draw_map
from input_for_david import generate_lists_for_map


def make_map(tobjects):

    data = generate_lists_for_map(tobjects)
    draw_map(data[0], data[1], data[2])
    return 0
