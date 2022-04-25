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
        uniform vec4 color;
        void main(){
            gl_FragColor = color;
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

vertices = np.zeros(9, [("position", np.float32, 2)])
vertices["position"] = [
    (-0.25, -0.1),
    (-0.25, -0.04),
    (-0.2, 0),
    (-0.15, 0),
    (-0.1, 0.05),
    (0.1, 0.05),
    (0.2, 0),
    (0.25, 0),
    (0.25, -0.1)
]

cont = 0
wheel_in = np.zeros(6, [("position", np.float32, 2)])
wheel = np.zeros(360, [("position", np.float32, 2)])
for i in range(360):
    fX = math.sin(i * DEG_IN_RAD) * 0.05 - 0.15
    fY = math.cos(i * DEG_IN_RAD) * 0.05 - 0.1
    wheel['position'][i] = (fX, fY)

    if i%60 == 0:
        wheel_in['position'][cont] = (fX, fY)
        cont = cont + 1

cont = 0
wheel_in2 = np.zeros(6, [("position", np.float32, 2)])
wheel2 = np.zeros(360, [("position", np.float32, 2)])
for i in range(360):
    fX = math.sin(i * DEG_IN_RAD) * 0.05 + 0.15
    fY = math.cos(i * DEG_IN_RAD) * 0.05 - 0.1
    wheel2['position'][i] = (fX, fY)

    if i%60 == 0:
        wheel_in2['position'][cont] = (fX, fY)
        cont = cont + 1

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

loc_color = glGetUniformLocation(program, "color")

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
    glUniformMatrix4fv(loc, 1, GL_TRUE, mat_transform)
    glUniform4f(loc_color, 0.0, 1.0, 0.0, 1.0)
    glDrawArrays(GL_POLYGON, 0, len(vertices))

    buffer = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, buffer)
    glBufferData(GL_ARRAY_BUFFER, wheel.nbytes, wheel, GL_DYNAMIC_DRAW)
    stride = wheel.strides[0]
    offset = ctypes.c_void_p(0)
    loc = glGetAttribLocation(program, "position")
    glEnableVertexAttribArray(loc)
    glVertexAttribPointer(loc, 2, GL_FLOAT, False, stride, offset)
    loc = glGetUniformLocation(program, "mat")
    glUniformMatrix4fv(loc, 1, GL_TRUE, mat_transform)
    glUniform4f(loc_color, 1.0, 0.0, 0.0, 1.0)
    glDrawArrays(GL_POLYGON, 0, len(wheel))

    buffer = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, buffer)
    glBufferData(GL_ARRAY_BUFFER, wheel_in.nbytes, wheel_in, GL_DYNAMIC_DRAW)
    stride = wheel_in.strides[0]
    offset = ctypes.c_void_p(0)
    loc = glGetAttribLocation(program, "position")
    glEnableVertexAttribArray(loc)
    glVertexAttribPointer(loc, 2, GL_FLOAT, False, stride, offset)
    loc = glGetUniformLocation(program, "mat")
    glUniformMatrix4fv(loc, 1, GL_TRUE, mat_transform)
    glUniform4f(loc_color, 0.0, 0.0, 1.0, 1.0)
    glDrawArrays(GL_POLYGON, 0, len(wheel_in))

    buffer = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, buffer)
    glBufferData(GL_ARRAY_BUFFER, wheel2.nbytes, wheel2, GL_DYNAMIC_DRAW)
    stride = wheel2.strides[0]
    offset = ctypes.c_void_p(0)
    loc = glGetAttribLocation(program, "position")
    glEnableVertexAttribArray(loc)
    glVertexAttribPointer(loc, 2, GL_FLOAT, False, stride, offset)
    loc = glGetUniformLocation(program, "mat")
    glUniformMatrix4fv(loc, 1, GL_TRUE, mat_transform)
    glUniform4f(loc_color, 1.0, 0.0, 0.0, 1.0)
    glDrawArrays(GL_POLYGON, 0, len(wheel2))

    buffer = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, buffer)
    glBufferData(GL_ARRAY_BUFFER, wheel_in2.nbytes, wheel_in2, GL_DYNAMIC_DRAW)
    stride = wheel_in2.strides[0]
    offset = ctypes.c_void_p(0)
    loc = glGetAttribLocation(program, "position")
    glEnableVertexAttribArray(loc)
    glVertexAttribPointer(loc, 2, GL_FLOAT, False, stride, offset)
    loc = glGetUniformLocation(program, "mat")
    glUniformMatrix4fv(loc, 1, GL_TRUE, mat_transform)
    glUniform4f(loc_color, 0.0, 0.0, 1.0, 1.0)
    glDrawArrays(GL_POLYGON, 0, len(wheel_in2))

    glfw.swap_buffers(window)
glfw.terminate()
