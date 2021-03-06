from .base import *

def get_sun(position_x, position_y):
    
    def always_rotate(rot, offset):
        rot += offset
        return rot
    
    
    shouldDrawTriangle = True
    lastTriangle = 0
    triangleMaxDeg = 28
    degCounter = 0

    #x_pos = 0.5
    #y_pos = 0.8

    vertices = np.zeros(360, [("position", np.float32, 2)])
    vertices2 = np.zeros(360, [("position", np.float32, 2)])

    for i in range(360):
        fX = math.cos(i * DEG_IN_RAD) * 0.05 
        fY = math.sin(i * DEG_IN_RAD) * 0.05 
        vertices['position'][i] = (fX, fY)

    for i in range(360):
        if shouldDrawTriangle:
            if degCounter == 0:
                fX = math.cos(i * DEG_IN_RAD) * 0.06
                fY = math.sin(i * DEG_IN_RAD) * 0.06
                vertices2['position'][i] = (fX, fY)
            if degCounter == triangleMaxDeg/2:
                fX = math.cos(i * DEG_IN_RAD) * 0.08
                fY = math.sin(i * DEG_IN_RAD) * 0.08
                vertices2['position'][i] = (fX, fY)
            if degCounter == triangleMaxDeg:
                degCounter = 0
                lastTriangle = i
                shouldDrawTriangle = False
                fX = math.cos(i * DEG_IN_RAD) * 0.06
                fY = math.sin(i * DEG_IN_RAD) * 0.06
                vertices2['position'][i] = (fX, fY)
            degCounter = degCounter + 1

        else:
            fX = math.cos(i * DEG_IN_RAD) * 0.06
            fY = math.sin(i * DEG_IN_RAD) * 0.06
            vertices2['position'][i] = (fX, fY)
            if i - lastTriangle >= 5:
                shouldDrawTriangle = True

    vertices2 = vertices2[~np.all(vertices2['position'] == 0, axis=1)]

    sun_1 = {
        'vertex' : vertices,
        'translation' : (position_x, position_y),
        'rotation' : .0,
        'scaling' : (1., 1.),
        'color' : {"R":255/255,
                   "G":140/255, 
                   "B":  1/255,},
        'mode' : GL_POLYGON,
        'constant' : always_rotate
    }

    sun_2 = {
        'vertex' : vertices2,
        'translation' : (position_x, position_y),
        'rotation' : .0,
        'scaling' : (1., 1.),
        'color' : {"R":255/255,
                   "G":204/255, 
                   "B":51/255,},
        'mode' : GL_POLYGON,
        'constant': always_rotate
    }

    return [sun_2, sun_1]