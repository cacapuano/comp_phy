# runga kutta method of intergration
#just importing packages
from matplotlib import pyplot
import numpy as np

#constants
mass = 10 #kg; mass on the pendulum
length = 1 #m; length of the string
g = 9.81 #m/s^2; gravity!
init_theta = np.pi/4 #initial angle
init_omega = 0.0 #starting velocity

def pendulum_functions(t, position):
    theta = position
    omega = position
    dtheta_dt = omega
    domega_dt = -(g / length) * np.sin(theta)
    
    return np.array([dtheta_dt, domega_dt])
    

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
    theta_val[i + 1] = theta + (1/6) * (k1_theta + 2*k2_theta + 2*k3_theta + k4_theta)
    omega_val[i + 1] = omega + (1/6) * (k1_omega + 2*k2_omega + 2*k3_omega + k4_omega)


# Angle plot
plt.subplot(2, 1, 1)
plt.plot(t_values, theta_values, label='Angle (theta)', color='blue')
plt.title('Pendulum Motion')
plt.xlabel('Time (s)')
plt.ylabel('Angular Position (radians)')
plt.grid()
plt.legend()

# Angular velocity plot
plt.subplot(2, 1, 2)
plt.plot(t_values, omega_values, label='Angular Velocity (omega)', color='orange')
plt.title('Pendulum Velocity')
plt.xlabel('Time (s)')
plt.ylabel('Angular Velocity (rad/s)')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
