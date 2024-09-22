#just importing packages
from matplotlib import pyplot
import numpy 


#constants
mass = 10 #kg; mass on the pendulum
length = 1 #m; length of the string
g = 9.81 #m/s^2; gravity!
init_theta = np.pi/4 #initial angle
init_omega = 0.0 #starting velocity

#initial conditions
theta_val[0] = init_theta
omega_val[0] = init_omega

for i in range(steps -1):
    theta = theta_val[i]
    omega = omega_val[i]

