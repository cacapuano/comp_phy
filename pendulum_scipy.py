# Find the motion of a pendulum using SciPy

#importing packages
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constants
g = 9.81  # m/s^2 gravity
L = 1.0   # m length of the pendulum 

# system of equations
def pendulum_scipy(time, y):
    theta, omega = y  
    dydt = [omega, -g / L * np.sin(theta)]  # [dtheta/dt, domega/dt]
    return dydt

# initial conditions
init_theta = np.pi / 4  # initial angle
init_omega = 0.0        # initial angular velocity
y_0_scipy = [init_theta, init_omega]

time_span = (0, 10) 
time_eval = np.linspace(time_span[0], time_span[1], 10) 

solution = solve_ivp(pendulum_scipy, time_span, y_0_scipy, time_eval=time_eval)

# Plot the results
plt.figure(figsize=(10, 4))
plt.plot(solution.t, solution.y[0], label='Angular Position', color='blue')
plt.title('Pendulum Motion')
plt.xlabel('Time (s)')
plt.ylabel('Angular Position (rad)')
plt.legend()

plt.figure(figsize=(10, 4))
plt.plot(solution.t, solution.y[1], label='Angular Velocity (omega)', color='orange')
plt.title('Pendulum Velocity')
plt.xlabel('Time (s)')
plt.ylabel('Angular Velocity (rad/s)')
plt.legend()
plt.grid()
plt.show()
