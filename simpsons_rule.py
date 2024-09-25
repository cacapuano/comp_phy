#simpson's rule for integration
import numpy as np

#constants
e_0 = 8.85e-12 #C^2/Nm^2 permittivity of free space
q = 1e-6 # coulombs - charge of the conducting sphere
R = 3e-3 # radius of the sphere m

# Simpson's Rule parameters
a = 1          # Start of the interval
b = 3          # End of the interval
n = 1000       # Number of subintervals (must be even)


#work done moving conducting sphere integral
def work(r,q):
    e_0 = 8.85e-12
    return (e_0 / 2)((1 / (4 * np.pi * e_0)) * (q / r**2)**2)


# Ensure n is even
if n % 2 == 1:
    n += 1

# Calculate the width of each subinterval
h = (b - a) / n

# Simpson's Rule calculation
integral = work(a) + work(b)

for i in range(1, n, 2):
    integral += 4 * work(a + i * h)

for i in range(2, n-1, 2):
    integral += 2 * work(a + i * h )

integral *= h / 3

# Print the result
print(f"Approximate work done moving the conducting sphere from {a} to {b} using Simpson's Rule: {integral}")
