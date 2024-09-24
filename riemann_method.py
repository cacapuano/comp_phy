#riemann's sum method of integration

import numpy as np

#constants
e_0 = 8.85e-12 #C^2/Nm^2 permittivity of free space
q = 1e-6 # coulombs - charge of the conducting sphere
r = 3e-3 # radius of the sphere m

# Riemann Sum parameters
a = 1          # Start of the interval
b = 10          # End of the interval
n = 1000       # Number of subintervals
delta_x = (b - a) / n  # Width of each subinterval

#work done moving conducting sphere integral
def work(r,q):
    e_0 = 8.85e-12
    return (e_0/2)((1 / (4 * np.pi * e_0)) * (q / r**2)**2)


# Calculate the Riemann sum using right endpoints
riemann_sum = sum(work(a + i * delta_x , q) * delta_x for i in range(1, n + 1))

# Print the result
print(f"Approximate work done moving the conducting sphere from {a} to {b}: {riemann_sum}")



