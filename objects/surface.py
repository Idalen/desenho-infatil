from .base import *

def get_surface():
    surface = {
        "vertex" : make_pair_vec(
            [(-1.0, 0.25),
             (1.0, 0.25),
             (1.0, -1.0),
             (-1.0, -1.0)]
        ),
        "translation": (0,0),
        'rotation' : 0.0,
        'scaling' : (1., 1.),
        "color" : { "R":128.0/255,
                    "G":132.0/255, 
                    "B": 136.0/255},
        "mode" : GL_POLYGON
    } 

    return [surface]