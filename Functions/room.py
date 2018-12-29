from vpython import *


def room(height, width, length):
    # Making a room
    thickness = height / 1000

    # size of the walls
    size_floor = vector(width, thickness, length)
    size_wall = vector(thickness, height, length)
    size_back = vector(width, height, thickness)

    # positions of walls
    x = width / 2
    y = height / 2
    z = length / 2

    # create the walls
    left_wall = box(pos=vector(-x,0,0), size=size_wall, color=color.white)
    right_wall = box(pos=vector(x,0,0), size=size_wall, color=color.white)
    top = box(pos=vector(0,y,0), size=size_floor, color=color.white)
    floor = box(pos=vector(0,-y,0), size=size_floor, color=color.white)
    back_wall = square = box(pos=vector(0,0,-z), size=size_back, color=color.white)


room(10, 10, 10)
