# runga kutta method of intergration
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

#time parameters
dt = 0.01
max_time = 20
steps = int(max_time/dt)

#arrays
time_val = np.linspace(0, max_time, steps)
theta_val = []
omega_val = []


for i in range(steps -1):
    theta = theta_val[i] # current theta value
    omega = omega_val[i] # current omega value

    # runga kutta
    k1_theta = omega * dt 
    k1_omega = dt * (-g/L * np.sin(theta))

    k2_theta = dt * (omega + 0.5 * k1_omega)
    k2_omega = dt * (-g/L * np.sin(theta + 0.5 * k1_theta))

    k3_theta = dt * (omega + 0.5 * k2_omega)
    k3_omega = dt * (-g/L * np.sin(theta + 0.5 * k2_theta))

    k4_theta =  dt * (omega + 0.5 * k3_omega)
    k4_omega = dt * (-g/L * np.sin(theta + 0.5 * k3_theta))

    #update array with new theta and omega
    theta_val[i + 1] = theta + (1/6) * (k1_theta
