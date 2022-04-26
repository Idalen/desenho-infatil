from .base import *

def get_car(position_x, position_y):
    shouldDrawTriangle = True
    lastTriangle = 0
    triangleMaxDeg = 28
    degCounter = 0

    body = {
        'vertex' : make_pair_vec([
            (-0.25, -0.1),
            (-0.25, -0.04),
            (-0.2, 0),
            (-0.15, 0),
            (-0.1, 0.05),
            (0.1, 0.05),
            (0.2, 0),
            (0.25, 0),
            (0.25, -0.1)
        ]),
        'translation' : (position_x, position_y),
        'color' : {"R":.78,
                   "G":.39, 
                   "B":.33},
        'mode' : GL_POLYGON
    }

    cont = 0
    wheel_in = np.zeros(6, POSITION_DT)
    wheel = np.zeros(360, POSITION_DT)
    for i in range(360):
        fX = math.sin(i * DEG_IN_RAD) * 0.05 - 0.15
        fY = math.cos(i * DEG_IN_RAD) * 0.05 - 0.1
        wheel['position'][i] = (fX, fY)

        if i%60 == 0:
            wheel_in['position'][cont] = (fX, fY)
            cont = cont + 1

    cont = 0
    wheel_in2 = np.zeros(6, POSITION_DT)
    wheel2 = np.zeros(360, POSITION_DT)
    for i in range(360):
        fX = math.sin(i * DEG_IN_RAD) * 0.05 + 0.15
        fY = math.cos(i * DEG_IN_RAD) * 0.05 - 0.1
        wheel2['position'][i] = (fX, fY)

        if i%60 == 0:
            wheel_in2['position'][cont] = (fX, fY)
            cont = cont + 1

    wheel_in_color = {
        "R":.78,
        "G":.39, 
        "B":.33,
    }

    wheel_out_color = {
        "R":.78,
        "G":.39, 
        "B":.33
    }

    wheel_inside1 = {
        'vertex' : wheel_in,
        'translation' : (position_x, position_y),
        'color' : wheel_in_color,
        'mode' : GL_POLYGON,
    }

    wheel_inside2 = {
        'vertex' : wheel_in2,
        'translation' : (position_x, position_y),
        'color' : wheel_in_color,
        'mode' : GL_POLYGON,
    }

    wheel_outside1 = {
        'vertex' : wheel,
        'translation' : (position_x, position_y),
        'color' : wheel_out_color,
        'mode' : GL_POLYGON,
    }
    wheel_outside2 = {
        'vertex' : wheel2,
        'translation' : (position_x, position_y),
        'color' : wheel_out_color,
        'mode' : GL_POLYGON,
    }

    return [body, wheel_inside1, wheel_inside2, wheel_outside1, wheel_outside2]
