import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import math
DEG_IN_RAD = 3.14 / 180

# %%
glfw.init()
glfw.window_hint(glfw.VISIBLE, glfw.FALSE)
window = glfw.create_window(800, 800, "Transformação Geométrica", None, None)
glfw.make_context_current(window)
# %%
vertex_code = """
        attribute vec2 position;
        uniform mat4 mat;
        void main(){
            gl_Position = mat * vec4(position,0.0,1.0);
        }
        """
fragment_code = """
        void main(){
            gl_FragColor = vec4(1.0,0.0,0.0,1.0);
        }
        """

program = glCreateProgram()
vertex = glCreateShader(GL_VERTEX_SHADER)
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
# %%
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
print(vertices2)

# %%
x_inc = 0.0
y_inc = 0.0
r_inc = 0.0
s_inc = 1.0


def key_event(window, key, scancode, action, mods):
    global x_inc, y_inc, r_inc, s_inc
    if key == 263:
        x_inc -= 0.0001
    if key == 262:
        x_inc += 0.0001
    if key == 265:
        y_inc += 0.0001
    if key == 264:
        y_inc -= 0.0001
    if key == 65:
        r_inc += 0.1
    if key == 83:
        r_inc -= 0.1
    if key == 90:
        s_inc += 0.1
    if key == 88:
        s_inc -= 0.1


glfw.set_key_callback(window, key_event)
glfw.show_window(window)
# %%
t_x = 0.0
t_y = 0.0
angulo = 0.0
s_x = 1.0
s_y = 1.0


def multiplica_matriz(a, b):
    m_a = a.reshape(4, 4)
    m_b = b.reshape(4, 4)
    m_c = np.dot(m_a, m_b)
    c = m_c.reshape(1, 16)
    return c


while not glfw.window_should_close(window):
    t_x += x_inc
    t_y += y_inc
    angulo += r_inc
    s_x = s_inc
    s_y = s_inc
    c = math.cos(math.radians(angulo))
    s = math.sin(math.radians(angulo))
    glfw.poll_events()
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(1.0, 1.0, 1.0, 1.0)
    mat_rotation = np.array([c, -s, 0.0, 0.0,
                             s, c, 0.0, 0.0,
                             0.0, 0.0, 1.0, 0.0,
                             0.0, 0.0, 0.0, 1.0], np.float32)
    mat_scale = np.array([s_x, 0.0, 0.0, 0.0,
                          0.0, s_y, 0.0, 0.0,
                          0.0, 0.0, 1.0, 0.0,
                          0.0, 0.0, 0.0, 1.0], np.float32)
    mat_translation = np.array([1.0, 0.0, 0.0, t_x,
                                0.0, 1.0, 0.0, t_y,
                                0.0, 0.0, 1.0, 0.0,
                                0.0, 0.0, 0.0, 1.0], np.float32)
    mat_transform = multiplica_matriz(mat_translation, mat_rotation)
    mat_transform = multiplica_matriz(mat_transform, mat_scale)

    buffer = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, buffer)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_DYNAMIC_DRAW)
    stride = vertices.strides[0]
    offset = ctypes.c_void_p(0)
    loc = glGetAttribLocation(program, "position")
    glEnableVertexAttribArray(loc)
    glVertexAttribPointer(loc, 2, GL_FLOAT, False, stride, offset)
    loc = glGetUniformLocation(program, "mat")
    glUniformMatrix4fv(loc, 1, GL_TRUE, mat_translation)
    glDrawArrays(GL_POLYGON, 0, 360)

    buffer = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, buffer)
    glBufferData(GL_ARRAY_BUFFER, vertices2.nbytes, vertices2, GL_DYNAMIC_DRAW)
    stride2 = vertices2.strides[0]
    offset = ctypes.c_void_p(0)
    loc = glGetAttribLocation(program, "position")
    glEnableVertexAttribArray(loc)
    glVertexAttribPointer(loc, 2, GL_FLOAT, False, stride2, offset)
    loc = glGetUniformLocation(program, "mat")
    glUniformMatrix4fv(loc, 1, GL_TRUE, mat_translation)
    glDrawArrays(GL_LINE_STRIP, 0, 360)


    glfw.swap_buffers(window)
glfw.terminate()
