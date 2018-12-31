import math

# Constants
c = 3 * (10 ** 8) # m/s
R = 10973731.568508 # 1/m 
h = 6.626 * (10 ** -34) # Joule * seconds
electron_mass = 9.10938356 * (10 ** -31) # kg
electron_charge = 1.60217662 * (10 ** -19) # coulombs
electron_radius = 2.8179403227 * (10 ** -15) # meters
proton_mass = 1.6726219 * (10 ** -27) # kg 
proton_radius = 10 ** -15 # meters
bohr_radius = 5.29 * (10 ** -11) # meters, radius of H atom
# permittivity of free space
epsilon = 8.854 * (10 ** -12)
vel_constant = (2 * (electron_charge ** 2)) / (8 * epsilon * math.pi * electron_mass)

