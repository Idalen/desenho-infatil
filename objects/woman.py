from .base import *

def circle(n_vertex, radius):
    vertex = np.zeros(n_vertex, POSITION_DT)
    angle = 0.0
    for i in range(n_vertex):
        angle += 2*math.pi/n_vertex
        x = math.cos(angle) * radius
        y = math.sin(angle) * radius
        vertex['position'][i] = (x, y)
    return [vertex]

def get_woman(position_x, position_y):
    dress = {
        "vertex" : make_pair_vec(
            [( 0.0,  0.0), 
             (-0.3, -0.5),
             (+0.3, -0.5)]
        ),
        "translation": (position_x, position_y),
        'rotation' : 0.0,
        'scaling' : (0., 0.),
        "color" : { "R":1.,
                    "G":0., 
                    "B":0.},
        "mode" : GL_TRIANGLES
    } 

    left_leg = {
        "vertex" : make_pair_vec(
            [(-0.05, -0.5),
             (-0.05, -0.7),
             (-0.1, -0.5),
             (-0.1, -0.7)],
        ),
        "translation": (position_x, position_y),
        'rotation' : 0.0,
        'scaling' : (0., 0.),
        "color" : { "R":0.,
                    "G":0., 
                    "B":0.},
        "mode" : GL_TRIANGLE_STRIP
    }

    right_leg = {
        "vertex" : make_pair_vec(
            [(+0.05, -0.5),
             (+0.05, -0.7),
             (+0.1, -0.5),
             (+0.1, -0.7)]
        ),
        "translation": (position_x, position_y),
        'rotation' : 0.0,
        'scaling' : (0., 0.),
        "color" : { "R":0.,
                    "G":0., 
                    "B":0.},
        "mode" : GL_TRIANGLE_STRIP
    }

    left_arm = {
        "vertex" : make_pair_vec(
            [(-0.08, -0.2),
             (-0.08, -0.15),
             (-0.3, -0.2),
             (-0.3, -0.15)]
        ),
        "translation": (position_x, position_y),
        'rotation' : 0.0,
        'scaling' : (0., 0.),
        "color" : { "R":0.,
                    "G":0., 
                    "B":0.},
        "mode" : GL_TRIANGLE_STRIP
    }

    right_arm = {
        "vertex" : make_pair_vec(
            [(0.08, -0.2),
             (0.08, -0.15),
             (0.3, -0.2),
             (0.3, -0.15)]
        ),
        "translation": (position_x, position_y),
        'rotation' : 0.0,
        'scaling' : (0., 0.),
        "color" : { "R":0.,
                    "G":0., 
                    "B":0.},
        "mode" : GL_TRIANGLE_STRIP
    }

    head = {
        "vertex" : np.zeros(64, POSITION_DT),
        "translation": (position_x, position_y),
        'rotation' : 0.0,
        'scaling' : (0., 0.),
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
        head["vertex"][i]['position'] = (x, y) 

    return [left_leg, right_leg, left_arm, right_arm, dress, head]