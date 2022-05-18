from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(voxel_edges=0, exposure=2)
scene.set_floor(0, (1.0, 1.0, 1.0))
scene.set_background_color((0.5, 0.5, 0.4))
scene.set_directional_light((-1, 1, -1), 0.2, (1, 0.8, 0.6))


@ti.func
def create_block(pos, size, color, color_noise):
    for I in ti.grouped(
            ti.ndrange((pos[0], pos[0] + size[0]), (pos[1], pos[1] + size[1]),
                       (pos[2], pos[2] + size[2]))):
        scene.set_voxel(I, 1, color + color_noise * ti.random())

@ti.func
def creat_bei(a, b,chang,kuan):
    create_block(pos=ivec3(a,  0,b),
                    size=ivec3(chang, 40, kuan),
                    color=vec3(0.93,0.93,0.93),
                    color_noise=vec3(0))

@ti.func
def creat_xin(a,b,start,direction):
    for i in range(12):
        x=0 if i < 4 else (3-i) if i < 7 else ((9-2*i))
        create_block(pos=ivec3(a-direction*i, b+i,40),
                        size=ivec3(1, start+x, 1),
                        color=vec3(0.85,0.05,0.05),
                        color_noise=vec3(0))

@ti.func
def creat_dianxin(a,b,c,length,height):
    create_block(pos=ivec3(a,b,c),
                    size=ivec3(length, height, length),
                    color=vec3(0.83,0.61,0.14),
                    color_noise=vec3(0))
    for i in range(40):
        x = int(ti.random() * ((a-1) -(a+length-1))) + (a+length-1)
        y = int(ti.random() * ((b-1) - (b+height-1))) + (b+height-1)
        z = int(ti.random() * ((c-1) - (c+length-1))) + (c+length-1)
        create_block(pos=ivec3(x,y,z),
                        size=ivec3(1, 1, 1),
                        color=vec3(0.21,0.12,0.05),
                        color_noise=vec3(0))
    

@ti.kernel
def initialize_voxels():
    creat_bei(0, 0,40,2)
    creat_bei(0, 0,2,40)
    creat_bei(39,0,2,40)
    creat_bei(0, 39,40,2)
    create_block(pos=ivec3(2,  0,2),
                    size=ivec3(36, 34.3, 36),
                    color=vec3(0.65,0.48,0.36),
                    color_noise=vec3(0))
    create_block(pos=ivec3(40, 30,20),
                    size=ivec3(10, 2, 6),
                    color=vec3(0.93,0.93,0.93),
                    color_noise=vec3(0))
    create_block(pos=ivec3(40, 15,20),
                    size=ivec3(10, 2, 6),
                    color=vec3(0.93,0.93,0.93),
                    color_noise=vec3(0))
    create_block(pos=ivec3(50, 15,20),
                    size=ivec3(2, 17, 6),
                    color=vec3(0.93,0.93,0.93),
                    color_noise=vec3(0))
    creat_xin(20,10,20,1)
    creat_xin(20,10,20,-1)
    creat_dianxin(-50, 0,0,40,3)
    creat_dianxin(-64, 3,0,40,3)


initialize_voxels()

scene.finish()
