from .base import *
 
def _update_trunk(translation, rotation, scaling, key):
    if key == 265:
        translation = (translation[0], translation[1]-0.00125)
    if key == 264:
        translation = (translation[0], translation[1]-0.00125)
    if key == 90:
        scaling = (scaling[0], scaling[1]+0.005)
    if key == 88:
        scaling = (scaling[0], scaling[1]-0.005)
        
    return translation, rotation, scaling

def _update_leaves(translation, rotation, scaling, key):
    if key == 265:
        translation = (translation[0], translation[1]+0.0005)
    if key == 264:
        translation = (translation[0], translation[1]-0.0005)
    if key == 90:
        scaling = (scaling[0], scaling[1]+0.005)
    if key == 88:
        scaling = (scaling[0], scaling[1]-0.005)
    
    return translation, rotation, scaling
def get_tree(position_x, position_y):
    
    trunk = {
        "vertex" : make_pair_vec([
            (-0.025, -0.35),
            (+0.025, -0.35),
            (+0.025, +0.35),
            (-0.025, +0.35)
        ]),
        "translation": (position_x, position_y),
        'rotation' : 0.0,
        'scaling' : (1., 1.),
        "color" : { "R":164.0/255,
                    "G":116.0/255,
                    "B": 73.0/255},
        "mode" : GL_POLYGON,
        "update": _update_trunk
    }

    leaves = {
        "vertex" : make_pair_vec([
            (+0.05, 0.25),
            (0, 0.75), 
            (-0.05, 0.25)
        ]),
        "translation": (position_x, position_y),
        'rotation' : 0.0,
        'scaling' : (1., 1.),
        "color" : { "R":97.0/255,
                    "G":138.0/255, 
                    "B":61.0/255},
        "mode" : GL_TRIANGLES,
        "update": _update_leaves

    }

    return [trunk, leaves]