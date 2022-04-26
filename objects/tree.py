from .base import *

def get_tree(position_x, position_y):
    trunk = {
        "vertex" : make_pair_vec([(+0.0, +0.0),
                                  (+0.1, +0.0), 
                                  (+0.1, +0.5),
                                  (+0.0, +0.5)]),
        "translation": (position_x, position_y),
        "color" : { "R":164.0/255,
                    "G":116.0/255, 
                    "B": 73.0/255},
        "mode" : GL_POLYGON
    } 

    leaves = {
        "vertex" : make_pair_vec([(-0.2, 0.5),
                                  (0.05, 1.5), 
                                  (0.3, 0.5)]),
        "translation": (position_x, position_y),
        "color" : { "R":97.0/255,
                    "G":138.0/255, 
                    "B":61.0/255},
        "mode" : GL_TRIANGLES
    } 

    return [trunk, leaves]