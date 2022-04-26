from .base import *

def get_surface():
    surface = {
        "vertex" : [(-1.0, 0.25),
                    (0.25, 0.25),
                    (0.25, -1.0),
                    (-1.0, -1.0)],
        "translation": (0,0),
        "color" : { "R":128.0/255,
                    "G":132.0/255, 
                    "B": 136.0/255},
        "mode" : GL_POLYGON
    } 

    return [surface]