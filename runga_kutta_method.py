# runga kutta method of intergration
#just importing packages
from matplotlib import pyplot as plt
import numpy as np

# constants
g = 9.81  # gravity m/s^2
length = 1.0   # length of the pendulum m

# ODE of Pendulum
def pendulum(time, position):
    theta, omega = position #creating vector that combines theta and omega
    dtheta_dt = omega #theta derivative
    domega_dt = - (g / length) * np.sin(theta) #omega derivative
    return np.array([dtheta_dt, domega_dt])

def pendulum_air_resistance(time, position):
    b = 0.5 #damping coeffience from air resistance
    theta, omega = position
    dtheta_dt = omega
    domega_dt = - (g / length) * np.sin(theta) - b * omega
    return np.array([dtheta_dt, domega_dt])


# runga-Kutta
def runga_kutta(function, y_0, init_time, max_time, dt):
    time_val = np.arange(init_time, max_time, dt) #total time of simulation
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

# runga-Kutta with air resistance
def a_runga_kutta(function, y_0, init_time, max_time, dt):
    a_time_val = np.arange(init_time, max_time, dt)
    a_y_val = np.zeros( (len(time_val), len(y_0)))
    a_y_val[0] = y_0

    for i in range(1, len(a_time_val)):
        time = a_time_val[i-1]
        y = a_y_val[i-1]

        # 4 coeffients
        k1 = function(time, y)
        k2 = function(time + dt/2, y + dt/2 * k1)
        k3 = function(time + dt/2, y + dt/2 * k2)
        k4 = function(time + dt, y + dt * k3)

        #sum coeffients
        a_y_val[i] = y + (dt/6) * (k1 + 2*k2 + 2*k3 + k4)

    return a_time_val, a_y_val


# initial conditions of the pendulum  
init_theta = np.pi / 4  # Initial angle (45 degrees but actual units are radians)
init_omega = 0.0        # Initial angular velocity rad/s
y_0 = np.array([init_theta, init_omega])

init_time = 0.0  # start time
max_time = 10.0  # end time
dt = 0.01  # time step

time_val, y_val = runga_kutta(pendulum, y_0, init_time, max_time, dt) # no air resistance

a_time_val, a_y_val = a_runga_kutta(pendulum_air_resistance, y_0, init_time, max_time, dt) #air resistance

# breaking up array
# no air resistance
theta_val = y_val[:, 0]
omega_val = y_val[:, 1]

# air resistance
a_theta_val = a_y_val[:, 0]
a_omega_val = a_y_val[:, 1]        

#analytic solution

t_values = np.arange(init_time, max_time, dt)
theta_values = init_theta * np.cos(np.sqrt(g / length) * t_values)
omega_values = -np.sqrt(g/length)*init_theta * np.sin(np.sqrt(g / length) * t_values)
 

# truncation error
truncation_errors_theta = (theta_val-theta_values)
truncation_errors_omega = (omega_val-omega_values)

#plot

plt.figure(figsize=(12, 6))

# angular position

plt.subplot(2, 1, 1)
plt.plot(time_val, theta_val, label='Without Air Reistance', color='orange')
plt.plot(a_time_val, a_theta_val, label='With Air Reistance', color='blue')
plt.title('Approximate Motion of the Pendulum Using Runga-Kutta')
plt.xlabel('Time (s)')
plt.ylabel('Angular Position of the Pendulum (radians)')
plt.grid()
plt.legend()

# Angular velocity plot

plt.subplot(2, 1, 2)
plt.plot(time_val, omega_val, label='Without Air Resistance', color='orange')
plt.plot(a_time_val, a_omega_val, label='With Air Resistance', color='blue')
plt.title('Approximate Velocity of the Pendulum Using Runga-Kutta')
plt.xlabel('Time (s)')
plt.ylabel('Angular Velocity (rad/s)')
plt.grid()
plt.legend()


plt.tight_layout()
plt.show()
        

#truncation error plot

plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)

plt.plot(time_val, truncation_errors_theta, label='Truncation Error', color='red')
plt.title('Truncation Error of the Angular Position')
plt.xlabel('Time (s)')
plt.ylabel('Error (radians)')
plt.legend()
plt.grid()

plt.subplot(2, 1, 2)

plt.plot(time_val, truncation_errors_omega, label='Truncation Error', color='red')
plt.title('Truncation Error of the Angular Velocity') 
plt.xlabel('Time (s)')
plt.ylabel('Error (radians/s)')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
    

