from .base import *

def get_house(position_x, position_y):
  building = {
      "vertex":make_pair_vec([(-0.7, 0.25),
                              (-0.7, 0.5), 
                              (-0.4, 0.5),
                              (-0.4, 0.25)]),
      "translation":(position_x, position_y),
      'rotation' : 0.0,
      "color":{"R":255.0/255,
              "G":255.0/255, 
              "B":240.0/255},
      "mode": GL_POLYGON
  }

  roof = {
      "vertex":make_pair_vec([(-0.7, 0.5),
                              (-0.55, 0.65), 
                               (-0.4, 0.5)]),
      "translation":(position_x, position_y),
      'rotation' : 0.0,
      "color":{"R":120.0/255,
              "G":49.0/255, 
              "B":20.0/255},
      "mode": GL_TRIANGLES      
  }

  door = {
      "vertex":make_pair_vec([(-0.5, 0.25),
                              (-0.5, 0.45), 
                              (-0.45, 0.45),
                              (-0.45, 0.25)]),
      "translation":(position_x, position_y),
      'rotation' : 0.0,
      "color" : { "R":164.0/255,
                  "G":116.0/255,
                  "B": 73.0/255},
      "mode": GL_POLYGON 
  }

  return [building, roof, door]