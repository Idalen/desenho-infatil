import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np


def get_tree(position_x, position_y):
    trunk = {
        "vertex" : [(+0.0, +0.0),
                    (+0.1, +0.0), 
                    (+0.1, +0.5),
                    (+0.0, +0.5)],
        "translation": (position_x, position_y),
        "color" : { "R":164.0/255,
                    "G":116.0/255, 
                    "B": 73.0/255},
        "mode" : GL_POLYGON
    } 

    leaves = {
        "vertex" : [(-0.2, 0.5),
                    (0.05, 1.5  ), 
                    (0.3, 0.5)],
        "translation": (position_x, position_y),
        "color" : { "R":97.0/255,
                    "G":138.0/255, 
                    "B":61.0/255},
        "mode" : GL_TRIANGLES
    } 

    return [trunk, leaves]   


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