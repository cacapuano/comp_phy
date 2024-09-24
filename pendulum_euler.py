#euler's method for a simple pendulum

#import packages
import numpy as np
import matplotlib.pyplot as plt

#constants
mass = 10 #kg; mass on the pendulum
length = 1 #m; length of the string
g = 9.81 #m/s^2; gravity!
init_theta = np.pi/4 #initial angle radians
init_omega = 0.0 #starting velocity rad/s

#time parameters
dt = 0.01
max_time = 20 #seconds

#arrays
time_val = np.arange(0, max_time, dt) #time array
theta_val = []
omega_val = []

#initial conditions
theta_val[0] = init_theta
omega_val[0] = init_omega

#euler's method to update theta and omega

for i in range(1, len(time_val)):    
    theta_values[i + 1] = init_omega + dt * omega_val[i]
    omega_values[i + 1] = init_theta + dt * (-g / length * np.sin(theta_val[i]))
