import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import math

def circle(n_vertex, radius):
    vertex = np.zeros(n_vertex, [("position", np.float32, 2)])
    angle = 0.0
    for i in range(n_vertex):
        angle += 2*math.pi/n_vertex
        x = math.cos(angle) * radius
        y = math.sin(angle) * radius
        vertex['position'][i] = (x, y)
    return [vertex]

def get_woman(position_x, position_y):
    dress = {
        "vertex" : [( 0.0,  0.0), 
                    (-0.3, -0.5),
                    (+0.3, -0.5)],
        "translation": (position_x, position_y),
        "color" : { "R":1.,
                    "G":0., 
                    "B":0.},
        "mode" : GL_TRIANGLES
    } 

    left_leg = {
        "vertex" : [(-0.05, -0.5),
                    (-0.05, -0.7),
                    (-0.1, -0.5),
                    (-0.1, -0.7)],
        "translation": (position_x, position_y),
        "color" : { "R":0.,
                    "G":0., 
                    "B":0.},
        "mode" : GL_TRIANGLE_STRIP
    }

    right_leg = {
        "vertex" : [(+0.05, -0.5),
                    (+0.05, -0.7),
                    (+0.1, -0.5),
                    (+0.1, -0.7)],
        "translation": (position_x, position_y),
        "color" : { "R":0.,
                    "G":0., 
                    "B":0.},
        "mode" : GL_TRIANGLE_STRIP
    }

    left_arm = {
        "vertex" : [(-0.08, -0.2),
                    (-0.08, -0.15),
                    (-0.3, -0.2),
                    (-0.3, -0.15)],
        "translation": (position_x, position_y),
        "color" : { "R":0.,
                    "G":0., 
                    "B":0.},
        "mode" : GL_TRIANGLE_STRIP
    }

    right_arm = {
        "vertex" : [(0.08, -0.2),
                    (0.08, -0.15),
                    (0.3, -0.2),
                    (0.3, -0.15)],
        "translation": (position_x, position_y),
        "color" : { "R":0.,
                    "G":0., 
                    "B":0.},
        "mode" : GL_TRIANGLE_STRIP
    }

    head = {
        "vertex" : [],
        "translation": (position_x, position_y),
        "color" : { "R":0.,
                    "G":0., 
                    "B":0.},
        "mode" : GL_TRIANGLE_FAN

    }
    n_vertex = 64
    radius = 0.15
    angle = 0.0
    for i in range(n_vertex):
        angle += 2*math.pi/n_vertex
        x = math.cos(angle) * radius
        y = math.sin(angle) * radius
        head["vertex"].append((x, y)) 

    return [left_leg, right_leg, left_arm, right_arm, dress, head]