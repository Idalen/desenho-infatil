from .base import *

def get_sun(position_x, position_y):
    shouldDrawTriangle = True
    lastTriangle = 0
    triangleMaxDeg = 28
    degCounter = 0

    vertices = np.zeros(360, [("position", np.float32, 2)])
    vertices2 = np.zeros(360, [("position", np.float32, 2)])

    for i in range(360):
        fX = math.sin(i * DEG_IN_RAD) * 0.05
        fY = math.cos(i * DEG_IN_RAD) * 0.05
        vertices['position'][i] = (fX, fY)

    for i in range(360):
        if shouldDrawTriangle:
            if degCounter == 0:
                fX = math.sin(i * DEG_IN_RAD) * 0.06
                fY = math.cos(i * DEG_IN_RAD) * 0.06
                vertices2['position'][i] = (fX, fY)
            if degCounter == triangleMaxDeg/2:
                fX = math.sin(i * DEG_IN_RAD) * 0.08
                fY = math.cos(i * DEG_IN_RAD) * 0.08
                vertices2['position'][i] = (fX, fY)
            if degCounter == triangleMaxDeg:
                degCounter = 0
                lastTriangle = i
                shouldDrawTriangle = False
                fX = math.sin(i * DEG_IN_RAD) * 0.06
                fY = math.cos(i * DEG_IN_RAD) * 0.06
                vertices2['position'][i] = (fX, fY)
            degCounter = degCounter + 1

        else:
            fX = math.sin(i * DEG_IN_RAD) * 0.06
            fY = math.cos(i * DEG_IN_RAD) * 0.06
            vertices2['position'][i] = (fX, fY)
            if i - lastTriangle >= 5:
                shouldDrawTriangle = True

    vertices2 = vertices2[~np.all(vertices2['position'] == 0, axis=1)]

    sun_1 = {
        'vertex' : vertices,
        'translation' : (position_x, position_y),
        'rotation' : 0.0,
        'color' : {"R":.78,
                   "G":.39, 
                   "B":.33,},
        'mode' : GL_POLYGON,
    }

    sun_2 = {
        'vertex' : vertices2,
        'translation' : (position_x, position_y),
        'rotation' : 0.0,
        'color' : {"R":.78,
                   "G":.39, 
                   "B":.33,},
        'mode' : GL_POLYGON,
    }

    return [sun_1, sun_2]