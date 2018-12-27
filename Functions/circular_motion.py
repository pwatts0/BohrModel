from vpython import *
import math

# With this function, we can make any object rotate along a circular axis
# If velocity is m/s, then radius is in meters and time is in seconds


def circular_motion(radius, velocity, time, axis):
    r = radius
    v = velocity
    # omega is change in angle divided by change in time 
    # radius * omega = velocity, so we rearrange to get omega = velocity / radius
    omega = v / r
    
    # Position = rCos(omega * t) + rSin(omega * t)
    cos_value = math.cos(omega * time)
    sin_value = math.sin(omega * time)
    # This would be the x and y values for the xy axis 
    axis_one = (r * cos_value)
    axis_two = (r * sin_value)
    
    # New Position in vector form
    # Determine which axis to rotate about
    if axis == 'xy':
        new_position = vector(axis_one, axis_two, 0)
    elif axis == 'xz':
        new_position = vector(axis_one, 0, axis_two)
    elif axis == 'yz':
        new_position = vector(0, axis_one, axis_two)

    return new_position


# This is an example of how to use the function
# First we set a radius, create a ring object, and create an object to rotate around the ring
# We will rotate about the xy axis in a radius of 100
radius = 100
ring = ring(pos=vector(0, 0, 0), radius=radius, axis=vector(0, 0, 1), color=color.white, thickness=.5)
ball = sphere(pos=vector(radius,0,0), radius = 5, color=color.green)

# Next, we will determine a rate, a change in time, and a starting time
# In vpython, a calling rate(60) means the calculation will happen every 1/60 seconds
# We determine the change in time, dt, using the rate
# By doing this, the change of time in the simulation matches the actual change in time of the program 

the_rate = 60
dt = 1 / the_rate
t = 1

while True:
    # We change the time and then call the function to update the position of our object
    t += dt
    ball.pos = circular_motion(radius, 100, t, 'xy')
    rate(the_rate)
