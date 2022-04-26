import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
from objects import *

def init_window():
    glfw.init()
    glfw.window_hint(glfw.VISIBLE, glfw.FALSE)
    window = glfw.create_window(1200, 600, "Main", None, None)
    glfw.make_context_current(window)

    return window

def init_program():
    vertex_code = """
            attribute vec2 position;
            uniform mat4 mat_transformation;
            void main(){
                gl_Position = mat_transformation*vec4(position,0.0,1.0);
            }
            """

    fragment_code = """
            uniform vec4 color;
            void main(){
                gl_FragColor = color;
            }
            """

    program  = glCreateProgram()
    vertex   = glCreateShader(GL_VERTEX_SHADER)
    fragment = glCreateShader(GL_FRAGMENT_SHADER)

    glShaderSource(vertex, vertex_code)
    glShaderSource(fragment, fragment_code)

    glCompileShader(vertex)
    if not glGetShaderiv(vertex, GL_COMPILE_STATUS):
        error = glGetShaderInfoLog(vertex).decode()
        print(error)
        raise RuntimeError("Erro de compilacao do Vertex Shader")

    glCompileShader(fragment)
    if not glGetShaderiv(fragment, GL_COMPILE_STATUS):
        error = glGetShaderInfoLog(fragment).decode()
        print(error)
        raise RuntimeError("Erro de compilacao do Fragment Shader") 

    glAttachShader(program, vertex)
    glAttachShader(program, fragment)

    glLinkProgram(program)
    if not glGetProgramiv(program, GL_LINK_STATUS):
        print(glGetProgramInfoLog(program))
        raise RuntimeError('Linking error')
        
    glUseProgram(program)

    return program

def buffer_data(program,vertices):
    buffer = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, buffer)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_DYNAMIC_DRAW)
    glBindBuffer(GL_ARRAY_BUFFER, buffer)

    stride = vertices.strides[0]
    offset = ctypes.c_void_p(0)

    loc = glGetAttribLocation(program, "position")
    glEnableVertexAttribArray(loc)

    glVertexAttribPointer(loc, 2, GL_FLOAT, False, stride, offset)


def main():
    window = init_window()
    program = init_program()

    objects = []
    objects+=(tree.get_tree(0, 0))
    objects+=(house.get_house(0.0, 0.0))
    objects+=(surface.get_surface())
    total_vertices = []
    for obj in objects:
        total_vertices+=obj['vertex']

    print(total_vertices)
    vertices = np.zeros(len(total_vertices), [('position', np.float32, 2)])
    # print(repr(vertices))
    vertices['position'] = total_vertices
    # print(repr(vertices))

    buffer_data(program, vertices)

    loc_color = glGetUniformLocation(program, "color")
    glfw.show_window(window)

    while not glfw.window_should_close(window):

        glfw.swap_buffers(window)
        glfw.poll_events() 
        
        glClear(GL_COLOR_BUFFER_BIT) 
        glClearColor(135/255, 206/255, 235/255, 1.0)

        vertex_acc = 0
        for obj in objects:

            mat_translation = np.array([1.0, 0.0, 0.0, obj["translation"][0], 
                                        0.0, 1.0, 0.0, obj["translation"][1], 
                                        0.0, 0.0, 1.0, 0.0, 
                                        0.0, 0.0, 0.0, 1.0], np.float32)
        
            loc = glGetUniformLocation(program, "mat_transformation")
            glUniformMatrix4fv(loc, 1, GL_TRUE, mat_translation)

            glUniform4f(loc_color, obj['color']['R'], obj['color']['G'], obj['color']['B'], 1.0)
            glDrawArrays(obj['mode'], vertex_acc, len(obj['vertex']))
            vertex_acc += len(obj['vertex'])


    glfw.terminate()


if __name__ == "__main__":
    main()
