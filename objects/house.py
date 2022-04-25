from .base import *

def get_house(position_x, position_y):
    building = {
        "vertex":[(0.0, 0.0),
                (0.0, 0.25), 
                (0.5, 0.25),
                (0.5, 0.0)],
        "translation":(position_x, position_y),
        "color":{"R":97.0/255,
                "G":138.0/255, 
                "B":61.0/255},
        "mode": GL_POLYGON
    }

    roof = {
        "vertex":[(0.0, 0.25),
                (0.25, 0.4  ), 
                (0.5, 0.25)],
        "translation":(position_x, position_y),
        "color":{"R":97.0/255,
                "G":138.0/255, 
                "B":61.0/255},
        "mode": GL_TRIANGLES      
    }

    door = {
        "vertex":[(0.1, 0.0),
                (0.1, 0.2), 
                (0.15, 0.2),
                (0.15, 0.0)],
        "translation":(position_x, position_y),
        "color":{"R":97.0/255,
                "G":0/255, 
                "B":61.0/255},
        "mode": GL_POLYGON 
    }

    return [building, roof, door]