from vpython import *
import math
import Light, room, constants, circular_motion, select_orbit


def rydberg_equation(nf, ni):
    # This function finds the wavelength of photon released
    # 1/lambda = R * (1/nf^2 - 1/ni^2)
    # nf < ni for positive energy values
    difference = (1 / nf **2) - (1 / ni ** 2)
    wavelength = 1 / (constants.R * difference)
    return wavelength


def delta_energy(wavelength):
    # change in energy = h * frequency
    frequency = constants.c / wavelength
    return frequency * constants.h


def allowed_radius(n):
    # This function tells us the distance the orbits are from the nucleus
    bohr_radius = 5.29 * (10 ** -11)
    if n == 1:
        return bohr_radius * scale
    else:
        return (n ** 2) * bohr_radius * scale


def electron_scale():
    if increase_electron.value == 1:
        electron.radius = constants.electron_radius * scale
        electron_display.text = " electron size = " + size_1 + " Angstroms"

    if increase_electron.value == 2:
        electron.radius = constants.electron_radius * scale * 100
        electron_display.text = " electron size = " + size_2 + " Angstroms"

    if increase_electron.value == 3:
        electron.radius = constants.electron_radius * scale * 1000
        electron_display.text = " electron size = " + size_3 + " Angstroms"

    if increase_electron.value == 4:
        electron.radius = constants.electron_radius * scale * 5000
        electron_display.text = " electron size = " + size_4 + " Angstroms"



# To make the objects visible, we will use a scale factor
scale = 10 ** 16

# Create a room for the objects to be in
room.room(allowed_radius(6) * 2, allowed_radius(6) * 2, allowed_radius(6) * 2, color.black)

# Create the objects
# We will use the classical electron radius since the simulation treats the electron as a particle
electron_size = constants.electron_radius * scale
electron = sphere(pos=vector(allowed_radius(1), 0, 0), radius=electron_size, color=color.yellow)
proton = sphere(pos=vector(0, 0, 0), radius=constants.proton_radius * scale, color=color.red)


# Create the orbits
orbit_thickness= constants.electron_radius * scale * 50
ground_state = ring(pos=vector(0,0,0), axis=vector(0,0,1), radius=allowed_radius(1), thickness=orbit_thickness, color=color.white)
first_excited = ring(pos=vector(0,0,0), axis=vector(0,0,1), radius=allowed_radius(2), thickness=orbit_thickness,  color=color.white)
second_excited = ring(pos=vector(0,0,0), axis=vector(0,0,1), radius=allowed_radius(3), thickness=orbit_thickness, color=color.white)
third_excited = ring(pos=vector(0,0,0), axis=vector(0,0,1), radius=allowed_radius(4), thickness=orbit_thickness, color=color.white)
fourth_excited = ring(pos=vector(0,0,0), axis=vector(0,0,1), radius=allowed_radius(5), thickness=orbit_thickness, color=color.white)
fifth_excited = ring(pos=vector(0,0,0), axis=vector(0,0,1), radius=allowed_radius(6), thickness=orbit_thickness, color=color.white)

# The electron is very small, so a slider will be put in to increase its size for visibility
increase_electron = slider(step=1, min=1, max=4, value=1, bind=electron_scale)


# Display the size of the electron
# Different possible sizes
size_1 = str(round((electron.radius / scale) * (10 ** 10), 5))
size_2 = str(round((electron.radius / scale) * 100 * (10 ** 10), 5))
size_3 = str(round((electron.radius / scale) * 1000 * (10 ** 10), 5))
size_4 = str(round((electron.radius / scale) * 5000 * (10 ** 10), 5))

# Display the initial size of the electron
electron_display = wtext(pos=scene.caption_anchor)
electron_display.text = " electron size = " + size_1 + " Angstroms"

the_rate = 60
dt = 1 / the_rate
t = 1
prev_orbit = 1
orbit = 1
counter = 0
# Initiate the while loop

while True:
    # set a rate
    rate(the_rate)
    # Make the electron orbit
    t += dt
    # To keep track of the previous orbit, we set a counter to only change prev_orbit every other change of orbit
    if counter == 2:
        prev_orbit = orbit
        counter = 0
    # The electron orbits depending on which radio button is checked
    # to find velocity, we use (1 / 8 * pi * epsilon) * (e^2 / r) = 1/2 * electron_mass * v^2
    if select_orbit.first_button.checked:
        velocity = math.sqrt(constants.vel_constant * (1/allowed_radius(1))) * scale
        electron.pos = circular_motion.circular_motion(allowed_radius(1), velocity, t, 'xy')
        orbit = 1
        counter += 1

    elif select_orbit.second_button.checked:
        velocity = math.sqrt(constants.vel_constant * (1 / allowed_radius(2))) * scale
        electron.pos = circular_motion.circular_motion(allowed_radius(2), velocity, t, 'xy')
        orbit = 2
        counter += 1

    elif select_orbit.third_button.checked:
        velocity = math.sqrt(constants.vel_constant * (1 / allowed_radius(3))) * scale
        electron.pos = circular_motion.circular_motion(allowed_radius(3), velocity, t, 'xy')
        orbit = 3
        counter += 1

    elif select_orbit.fourth_button.checked:
        velocity = math.sqrt(constants.vel_constant * (1 / allowed_radius(4))) * scale
        electron.pos = circular_motion.circular_motion(allowed_radius(4), velocity, t, 'xy')
        orbit = 4
        counter += 1

    elif select_orbit.fifth_button.checked:
        velocity = math.sqrt(constants.vel_constant * (1 / allowed_radius(5))) * scale
        electron.pos = circular_motion.circular_motion(allowed_radius(5), velocity, t, 'xy')
        orbit = 5
        counter += 1

    elif select_orbit.sixth_button.checked:
        velocity = math.sqrt(constants.vel_constant * (1 / allowed_radius(6))) * scale
        electron.pos = circular_motion.circular_motion(allowed_radius(6), velocity, t, 'xy')
        orbit = 6
        counter += 1

    if prev_orbit != orbit:
        wavelength = rydberg_equation(orbit, prev_orbit) * (10 ** 9)
        emitted_light = color.black
        if 700 >= wavelength >= 635:
            emitted_light = color.red
        elif 634 >= wavelength >= 590:
            emitted_light = color.orange
        elif 589 >= wavelength >= 560:
            emitted_light = color.yellow
        elif 559 >= wavelength >= 520:
            emitted_light = color.green
        elif 519 >= wavelength >= 490:
            emitted_light = color.cyan
        elif 489 >= wavelength >= 450:
            emitted_light = color.blue
        elif 449 >= wavelength >= 400:
            emitted_light = color.purple

        Light.light(vector(0, 0, 0), emitted_light, .5)
