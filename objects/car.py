from .base import *

def get_car(position_x, position_y):

    def upd_func_body(trans, rot, scaling, keypress):
        if keypress == 263:
            trans = (trans[0] - 0.01, trans[1])
        elif keypress == 262:
            trans = (trans[0] + 0.01, trans[1])

        return trans, rot, scaling

    def upd_func_wheel(trans, rot, scaling,keypress):
        if keypress == 263:
            trans = (trans[0] - 0.01, trans[1])
        elif keypress == 262:
            trans = (trans[0] + 0.01, trans[1])
        elif keypress == 65:
            rot += 0.1
        elif keypress == 83:
            rot -= 0.1
        
        return trans, rot, scaling


    body = {
        'vertex' : make_pair_vec([
            (0.25, -0.1),
            (0.25, -0.04),
            (0.2, 0),
            (0.15, 0),
            (0.1, 0.05),
            (-0.1, 0.05),
            (-0.2, 0),
            (-0.25, 0),
            (-0.25, -0.1)
        ]),
        'translation' : (position_x, position_y),
        'rotation' : 0.0,

        'scaling' : (1., 1.),
        'color' : {"R":.78,
                   "G":.39, 
                   "B":.33},
        'mode' : GL_POLYGON,
        'update' : upd_func_body
    }

    def wheel(n_sides, radius):
        cont = 0
        wheel_in = np.zeros(n_sides, POSITION_DT)
        wheel = np.zeros(360, POSITION_DT)
        for i in range(360):
            fX = math.sin(i * DEG_IN_RAD) * radius
            fY = math.cos(i * DEG_IN_RAD) * radius
            wheel['position'][i] = (fX, fY)

            if i%(360/n_sides) == 0:
                wheel_in['position'][cont] = (fX, fY)
                cont = cont + 1

        return wheel, wheel_in

    wheel1, wheel_in1 = wheel(6, .05)
    wheel2, wheel_in2 = wheel(6, .05)
    
    wheel_in_color = {
        "R":.5,
        "G":.5, 
        "B":.5,
    }

    wheel_out_color = {
        "R":.0,
        "G":.0, 
        "B":.0
    }

    wheel_inside1 = {
        'vertex' : wheel_in1,
        'translation' : (position_x-0.15, position_y-0.10),
        'rotation' : 0.,
        'scaling' : (1., 1.),
        'color' : wheel_in_color,
        'mode' : GL_POLYGON,
        'update': upd_func_wheel
    }

    wheel_inside2 = {
        'vertex' : wheel_in2,
        'translation' : (position_x+0.15, position_y-0.10),
        'rotation' : 0.,
        'scaling' : (1., 1.),
        'color' : wheel_in_color,
        'mode' : GL_POLYGON,
        'update': upd_func_wheel
    }

    wheel_outside1 = {
        'vertex' : wheel1,
        'translation' : (position_x-0.15, position_y-0.10),
        'rotation' : 0.,
        'scaling' : (1., 1.),
        'color' : wheel_out_color,
        'mode' : GL_POLYGON,
        'update': upd_func_wheel
    }
    wheel_outside2 = {
        'vertex' : wheel2,
        'translation' : (position_x+0.15, position_y-0.10),
        'rotation' : 0.,
        'scaling' : (1., 1.),
        'color' : wheel_out_color,
        'mode' : GL_POLYGON,
        'update': upd_func_wheel
    }

    return [body, wheel_outside1, wheel_outside2, wheel_inside1, wheel_inside2]
