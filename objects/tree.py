from .base import *

def get_tree(position_x, position_y):
    
    trunk = {
        "vertex" : [(-0.675, +0.75),
                    (-0.625, +0.75),
                    (-0.625, +0.95),
                    (-0.675, +0.95)],
        "translation": (position_x, position_y),
        "color" : { "R":164.0/255,
                    "G":116.0/255,
                    "B": 73.0/255},
        "mode" : GL_POLYGON
    }

    leaves = {
        "vertex" : [(-0.7, 0.95),
                    (-0.65, 1.45), 
                    (-0.6, 0.95)],
        "translation": (position_x, position_y),
        "color" : { "R":97.0/255,
                    "G":138.0/255, 
                    "B":61.0/255},
        "mode" : GL_TRIANGLES
    }

    return [trunk, leaves]