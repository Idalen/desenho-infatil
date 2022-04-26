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
             (-0.06, -0.1),
             (+0.06, -0.1)]
        ),
        "translation": (position_x, position_y),
        'rotation' : 0.0,
        'scaling' : (1., 1.),
        "color" : { "R":1.,
                    "G":0., 
                    "B":0.},
        "mode" : GL_TRIANGLES
    } 

    left_leg = {
        "vertex" : make_pair_vec(
            [(-0.01, -0.1),
             (-0.01, -0.15),
             (-0.02, -0.1),
             (-0.02, -0.15)],
        ),
        "translation": (position_x, position_y),
        'rotation' : 0.0,
        'scaling' : (1., 1.),
        
        "color" : { "R":0.,
                    "G":0., 
                    "B":0.},
        "mode" : GL_TRIANGLE_STRIP
    }

    right_leg = {
        "vertex" : make_pair_vec(
            [(+0.01, -0.1),
             (+0.01, -0.15),
             (+0.02, -0.1),
             (+0.02, -0.15)]
        ),
        "translation": (position_x, position_y),
        'rotation' : 0.0,
        'scaling' : (1., 1.),
        
        "color" : { "R":0.,
                    "G":0., 
                    "B":0.},
        "mode" : GL_TRIANGLE_STRIP
    }

    left_arm = {
        "vertex" : make_pair_vec(
            [(-0.015, -0.04),
             (-0.015, -0.03),
             (-0.06, -0.04),
             (-0.06, -0.03)]
        ),
        "translation": (position_x, position_y),
        'rotation' : 0.0,
        'scaling' : (1., 1.),
        
        "color" : { "R":0.,
                    "G":0., 
                    "B":0.},
        "mode" : GL_TRIANGLE_STRIP
    }

    right_arm = {
        "vertex" : make_pair_vec(
            [(0.015, -0.04),
             (0.015, -0.03),
             (0.06, -0.04),
             (0.06, -0.03)]
        ),
        "translation": (position_x, position_y),
        'rotation' : 0.0,
        'scaling' : (1., 1.),
        
        "color" : { "R":0.,
                    "G":0., 
                    "B":0.},
        "mode" : GL_TRIANGLE_STRIP
    }

    n_vertex = 360
    radius = 0.03
    angle = 0.0
    
    head = {
        "vertex" : np.zeros(n_vertex, POSITION_DT),
        "translation": (position_x, position_y),
        'rotation' : 0.0,
        'scaling' : (1., 1.),
        
        "color" : { "R":0.,
                    "G":0., 
                    "B":0.},
        "mode" : GL_TRIANGLE_FAN

    }
    for i in range(n_vertex):
        angle += 2*math.pi/n_vertex
        x = math.cos(angle) * radius
        y = math.sin(angle) * radius
        head["vertex"][i]['position'] = (x, y) 

    return [left_leg, right_leg, left_arm, right_arm, dress, head]