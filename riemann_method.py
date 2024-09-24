#riemann's sum method of integration

import numpy as np

#constants
e_0 =
q =
r =

# Riemann Sum parameters
a = 1          # Start of the interval
b = 10          # End of the interval
n = 1000       # Number of subintervals
delta_x = (b - a) / n  # Width of each subinterval

#work done moving conducting sphere integral
def work(r,q):
    epislon_0 = 8.85e-12
    return (epsilon_0/2)((1 / (4 * np.pi * epsilon_0)) * (q / r**2)**2)


# Calculate the Riemann sum using right endpoints
riemann_sum = sum(f(a + i * delta_x) * delta_x for i in range(1, n + 1))

# Print the result
print(f"Approximate work done moving the conducting sphere from {a} to {b}: {riemann_sum}")



