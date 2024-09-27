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
init_time = 0.0 #seconds

def euler(init_theta, init_omega, init_time, max_time, dt):
    steps = int((max_time - init_time) / dt)

    e_time_val = np.zeros(steps)
    e_theta_val = np.zeros(steps)
    e_omega_val = np.zeros(steps)
    
    #initial conditions
    e_theta_val[0] = init_theta
    e_omega_val[0] = init_omega

    for i in range(1, steps):
        e_time_val[i] = e_time_val[i - 1] + dt 
        e_theta_val[i] = e_theta_val[i - 1] + e_omega_val[i - 1] * dt
        e_omega_val[i] = e_omega_val[i - 1] - (g / length) * np.sin(e_theta_val[i - 1]) * dt

    return e_time_val, e_theta_val, e_omega_val

#time parameters
dt = 0.01
max_time = 10 #seconds

# calculate
e_time_val, e_theta_val, e_omega_val = euler(init_theta, init_omega, init_time, max_time, dt)



# runga kutta method of intergration
# ODE of Pendulum
def pendulum(time, position):
    theta, omega = position
    dtheta_dt = omega
    domega_dt = - (g / length) * np.sin(theta)
    return np.array([dtheta_dt, domega_dt])

# runga-Kutta
def runga_kutta(function, y_0, init_time, max_time, dt):
    r_time_val = np.arange(init_time, max_time, dt)
    r_y_val = np.zeros( (len(r_time_val), len(y_0)))
    r_y_val[0] = y_0

    for i in range(1, len(r_time_val)):
        time = r_time_val[i-1]
        y = r_y_val[i-1]

        # 4 coeffients
        k1 = function(time, y)
        k2 = function(time + dt/2, y + dt/2 * k1)
        k3 = function(time + dt/2, y + dt/2 * k2)
        k4 = function(time + dt, y + dt * k3)

        #sum coeffients
        r_y_val[i] = y + (dt/6) * (k1 + 2*k2 + 2*k3 + k4)

    return r_time_val, r_y_val

# initial conditions of the pendulum  
init_theta = np.pi / 4  # Initial angle (45 degrees)
init_omega = 0.0        # Initial angular velocity
y_0 = np.array([init_theta, init_omega])

init_time = 0.0  # Start time
max_time = 10.0  # End time
dt = 0.01  # Time step

r_time_val, r_y_val = runga_kutta(pendulum, y_0, init_time, max_time, dt)

# breaking up array
r_theta_val = r_y_val[:, 0]
r_omega_val = r_y_val[:, 1]
        




# Plotting the results
plt.figure(figsize=(12, 6))

# Angle plot
plt.subplot(2, 1, 1)
plt.plot(e_time_val, e_theta_val, label='Euler Method', color = 'blue')
plt.plot(r_time_val, r_theta_val, label='Runga-Kutta', color = 'orange')
plt.title('Pendulum Motion')
plt.xlabel('Time (s)')
plt.ylabel('Angular Position (radians)')
plt.grid()
plt.legend()

# Angular velocity plot
plt.subplot(2, 1, 2)
plt.plot(e_time_val, e_omega_val, label='Euler Method', color='blue')
plt.plot(r_time_val, r_omega_val, label='Runga-Kutta', color='orange')
plt.title('Pendulum Motion')
plt.xlabel('Time (s)')
plt.ylabel('Angular Velocity (rad/s)')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
