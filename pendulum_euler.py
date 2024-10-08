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

    time_val = np.zeros(steps)
    theta_val = np.zeros(steps)
    omega_val = np.zeros(steps)
    
    #initial conditions
    theta_val[0] = init_theta
    omega_val[0] = init_omega

    for i in range(1, steps):
        time_val[i] = time_val[i - 1] + dt #time function 
        theta_val[i] = theta_val[i - 1] + omega_val[i - 1] * dt #theta functions
        omega_val[i] = omega_val[i - 1] - (g / length) * np.sin(theta_val[i - 1]) * dt # omega function

    return time_val, theta_val, omega_val

#time parameters
dt = 0.01
max_time = 10 #seconds

# calculate
time_val, theta_val, omega_val = euler(init_theta, init_omega, init_time, max_time, dt)


#analytic solution

t_values = np.arange(init_time, max_time, dt)
theta_values = init_theta * np.cos(np.sqrt(g / length) * t_values)
omega_values = -np.sqrt(g/length)*init_theta * np.sin(np.sqrt(g / length) * t_values)
 

# truncation error
truncation_errors_theta = (theta_val-theta_values)
truncation_errors_omega = (omega_val-omega_values)


# Plotting the results
plt.figure(figsize=(12, 6))

# Angle plot
plt.subplot(2, 1, 1)
plt.plot(time_val, theta_val, label='Angle (theta)', color='blue')
plt.title('Pendulum Motion')
plt.xlabel('Time (s)')
plt.ylabel('Angular Position (radians)')
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
    
