#simpson's rule for integration
import numpy as np

#constants
e_0 = 8.85e-12 #C^2/Nm^2 permittivity of free space
q = 1e-6 # coulombs - charge of the conducting sphere
R = 3e-3 # radius of the sphere m

# Simpson's Rule parameters
a = 1          # Start of the interval
b = 3          # End of the interval
interval = 1000       # Number of subintervals (must be even)


#work done moving conducting sphere integral
def work(r):
    e_0 = 8.85e-12
    top = e_0/2
    k = 1 / (4 * np.pi * e_0)
    E_field = (k * q / r**2)**2
    return top * E_field
  

def simpsons_rule(function, a, b, interval):

# Ensure n is even
    if interval % 2 == 1:
        interval += 1

# Calculate the width of each subinterval
    h = (b - a) / interval

# Simpson's Rule calculation
    integral = function(a) + function(b)

    for i in range(1, interval, 2):
        integral += 4 * function(a + i * h)

    for i in range(2, interval-1, 2):
        integral += 2 * function(a + i * h )

    integral *= h / 3
    return integral

# Integrate
Work_integrated_simpson = simpsons_rule(work, a, b, interval)


# Print the result
print(f"Approximate work done moving the conducting sphere from {a} to {b} using Simpson's Rule: {Work_integrated_simpson:e} N*m/C")
