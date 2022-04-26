from .base import *

def get_tree(position_x, position_y):
    def upd_func(trans, rot, keypress):
        if keypress == 263:
            trans = (trans[0] - 0.01, trans[1])
        elif keypress == 262:
            trans = (trans[0] + 0.01, trans[1])

        return trans, rot

    trunk = {
        "vertex" : make_pair_vec([(+0.0, +0.0),
                                  (+0.1, +0.0), 
                                  (+0.1, +0.5),
                                  (+0.0, +0.5)]),
        "translation": (position_x, position_y),
        'rotation' : (0, 0),
        "color" : { "R":164.0/255,
                    "G":116.0/255, 
                    "B": 73.0/255},
        "mode" : GL_POLYGON,
        'update' : upd_func
    } 

    leaves = {
        "vertex" : make_pair_vec([(-0.2, 0.5),
                                  (0.05, 1.5), 
                                  (0.3, 0.5)]),
        "translation": (position_x, position_y),
        'rotation' : (0, 0),
        "color" : { "R":97.0/255,
                    "G":138.0/255, 
                    "B":61.0/255},
        "mode" : GL_TRIANGLES,
        'update' : upd_func,
    } 

    return [trunk, leaves]