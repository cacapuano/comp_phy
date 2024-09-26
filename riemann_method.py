#riemann's sum method of integration

import numpy as np

#constants
e_0 = 8.85e-12 #C^2/Nm^2 permittivity of free space
q = 1e-6 # coulombs - charge of the conducting sphere
R = 3e-3 # radius of the sphere m

# Riemann Sum parameters
a = R          # Start of the interval
b = 3          # End of the interval
interval = 1000       # Number of subintervals
#delta_x = (b - a) / interval  # Width of each subinterval

# defining function to integrate over
def work(r):
    e_0 = 8.85e-12
    top = e_0/2
    k = 1 / (4 * np.pi * e_0)
    E_field = (k * q / r**2)**2
    return top * E_field

# riemann's sum definition
def riemann_sum(function, a, b, interval,  method = 'left'):
    h = (b - a) / interval  # Step size
    total_area = 0

    for i in range(interval):
        if method == 'left':
            x = a + i * h  # Left endpoint
        elif method == 'right':
            x = a + (i + 1) * h  # Right endpoint
        elif method == 'mid':
            x = a + (i + 0.5) * h  # Midpoint
        else:
            raise ValueError("Method must be 'left', 'right', or 'mid'")

        total_area += function(x) * h  # Area of the rectangle

    return total_area


# integrate
Work_integrated_riemann = riemann_sum(work, a, b, interval, method='left')


# Print the result
print(f"Approximate work done moving the conducting sphere from {a} to {b} using Riemann's Sum: {Work_integrated_riemann:e} N*m/C")



