# runga kutta method of intergration
#just importing packages
from matplotlib import pyplot as plt
import numpy as np

# constants
g = 9.81  # gravity m/s^2
length = 1.0   # length of the pendulum m

# ODE of Pendulum
def pendulum(time, position):
    theta, omega = position
    dtheta_dt = omega
    domega_dt = - (g / length) * np.sin(theta)
    return np.array([dtheta_dt, domega_dt])

# runga-Kutta
def runga_kutta(function, y_0, init_time, max_time, dt):
    time_val = np.arange(init_time, max_time, dt)
    y_val = np.zeros( (len(time_val), len(y_0)))
    y_val[0] = y_0

    for i in range(1, len(time_val)):
        time = time_val[i-1]
        y = y_val[i-1]

        # 4 coeffients
        k1 = function(time, y)
        k2 = function(time + dt/2, y + dt/2 * k1)
        k3 = function(time + dt/2, y + dt/2 * k2)
        k4 = function(time + dt, y + dt * k3)

        #sum coeffients
        y_val[i] = y + (dt/6) * (k1 + 2*k2 + 2*k3 + k4)

    return time_val, y_val

# initial conditions of the pendulum  
init_theta = np.pi / 4  # Initial angle (45 degrees)
init_omega = 0.0        # Initial angular velocity
y_0 = np.array([init_theta, init_omega])

init_time = 0.0  # Start time
max_time = 10.0  # End time
dt = 0.01  # Time step

time_val, y_val = runga_kutta(pendulum, y_0, init_time, max_time, dt)

# breaking up array
theta_val = y_val[:, 0]
omega_val = y_val[:, 1]
        



# plot

plt.figure(figsize=(12, 6))

# angular position

plt.subplot(2, 1, 1)
plt.plot(time_val, theta_val, label='Angle (theta)', color='blue')
plt.title('Pendulum Motion')
plt.xlabel('Time (s)')
plt.ylabel('Angular Position of the Pendulum (radians)')
plt.grid()
plt.legend()

# Angular velocity plot

plt.subplot(2, 1, 2)
plt.plot(time_val, omega_val, label='Angular Velocity (omega)', color='orange')
plt.title('Pendulum Motion')
plt.xlabel('Time (s)')
plt.ylabel('Angular Velocity (rad/s)')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
        

    
    

