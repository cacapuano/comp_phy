# runga kutta method of intergration
#just importing packages
from matplotlib import pyplot
import numpy as np

#constants
mass = 10 #kg; mass on the pendulum
length = 1 #m; length of the string
g = 9.81 #m/s^2; gravity!

# equations for the pendulum
def pendulum_functions(t, position):
    theta = position
    omega = position
    dtheta_dt = omega
    domega_dt = -(g / length) * np.sin(theta)
    
    return np.array([dtheta_dt, domega_dt])
    

#initial conditions
init_theta = np.pi/4 #initial angle
init_omega = 0.0 #starting velocity

#time parameters
dt = 0.01
init_time = 0.0 # seconds
max_time = 20


# vector array
y_0 = np.array([init_theta, init_omega])


# defining the runga-kutta method to the 4th order
def runga_kutta(function, y_0, init_time, max_time, dt):
    time_val = np.arange(init_time, max_time, dt)
    y_val = np.zeros((len(time_val), len(y_0)))
    y_val[0] = y_0

    for i in range(steps -1):
        time = time_val[i-1] 
        y = y_val[i-1]

        # runga-kutta coeffients
        k1 = function(t, y)
        k2 = function(t + dt/2, y + dt/2 * k1)
        k3 = function(t + dt/2, y + dt/2 * k2)
        k4 = function(t + dt, y + dt * k3)

        y_val[i] = y + (1/6) * (k1 + 2 * k2 + 2 * k3 + k4) * dt

    return y_val, time_val

# theta and omega arrays
theta_val = y_val[:, 0]
omega_val = y_val[:, 1]

time_val, y_val = runga_kutta(pendulum_functions, y_0, init_time, max_time, dt)






# Angle plot
plt.subplot(2, 1, 1)
plt.plot(time_val, theta_val, label='Angular Position (theta)', color='blue')
plt.title('Pendulum Motion')
plt.xlabel('Time (s)')
plt.ylabel('Angular Position (radians)')
plt.grid()
plt.legend()

# Angular velocity plot
plt.subplot(2, 1, 2)
plt.plot(time_val, omega_val, label='Angular Velocity (omega)', color='orange')
plt.title('Pendulum Velocity')
plt.xlabel('Time (s)')
plt.ylabel('Angular Velocity (rad/s)')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
