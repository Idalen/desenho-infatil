from .base import *

def get_tree(position_x, position_y):
    
    trunk = {
        "vertex" : make_pair_vec([(-0.875, +0.25),
                    (-0.825, +0.25),
                    (-0.825, +0.45),
                    (-0.875, +0.45)]),
        "translation": (position_x, position_y),
        "color" : { "R":164.0/255,
                    "G":116.0/255,
                    "B": 73.0/255},
        "mode" : GL_POLYGON
    }

    leaves = {
        "vertex" : make_pair_vec([(-0.9, 0.45),
                    (-0.85, 0.95), 
                    (-0.8, 0.45)]),
        "translation": (position_x, position_y),
        "color" : { "R":97.0/255,
                    "G":138.0/255, 
                    "B":61.0/255},
        "mode" : GL_TRIANGLES
    }

    return [trunk, leaves]