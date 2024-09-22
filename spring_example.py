from matplotlib import pyplot
import numpy

#constants
x = 20 #starting position
v_x = 0 #starting velocity
init_time = 0 #starting time
iteration = 0
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

def implicit(x, velocity, force, dt):
    acceleration = force/mass
    new_velocity = v_x + acceleration*dt
    new_position = x + v_x*dt
    return new_position, new_velocity

    for label, update in zip(['Explicit', 'Implicit'],
                             [explicit, implicit]):


    while iteration < 1000:
        position_x.append(x)
        time.append(init_time)

        tot_force = force(x)
        x, v_x = update(x, v_x, tot_force, dt)
        time += 1


pyplot.plot(time, position_x)

pyplot.legend()
pyplot.xlabel('Time')
pyplot.ylabel('X position')
pyplot.show()
