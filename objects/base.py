import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import math

POSITION_DT = np.dtype([('position', np.float32, 2)])
DEG_IN_RAD = math.pi / 180.0

def make_pair_vec(v):
    arr = np.zeros(len(v), POSITION_DT)
    arr['position'] = v
    return arr.copy() 