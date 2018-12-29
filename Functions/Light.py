from vpython import *
import room


def light(position, color, duration):
    # Create a local light
    lamp = local_light(pos=position, color=color)
    # How long the light will stay
    time.sleep(duration)
    # Make the light will go away
    lamp.visible = False


# Create a room with our room function
room.room(10, 10, 10, color.white)
# sleep so the light function can be seen
time.sleep(2)
# Create a blue light for 2 seconds at the origin
light(vector(0, 0, 0), color.blue, 2)






