import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import math

DEG_IN_RAD = math.pi / 180.0

def make_pair_vec(v):
    dt = np.dtype([('position', np.float32, 2)])
    arr = np.zeros(len(v), dt)
    arr['position'] = v
    return arr.copy() 