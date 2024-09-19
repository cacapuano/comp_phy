from matplotlib import pyplot
import numpy

#constants
x = 20 #starting position
v_x = 0 #starting velocity
init_time = 0 #starting time
mass = 500 #kg
k = 100 #spring constant

#arrays for plotting
time = []
position_x = []

def force(x):
    return -k*x

def explicit(x, velocity, force, dt):
    acceleration = force/mass
    new_position = x + v_x*dt
    new_velocity = v_x + acceleration*dt
    return new_position, new_velocity


