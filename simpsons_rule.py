#simpson's rule for integration
import numpy as np

#constants
e_0 =
q =
r =

# Simpson's Rule parameters
a = 1          # Start of the interval
b = 3          # End of the interval
n = 1000       # Number of subintervals (must be even)


#work done moving conducting sphere integral
def work(r,q):
    epislon_0 = 8.85e-12
    return (epsilon_0/2)((1 / (4 * np.pi * epsilon_0)) * (q / r**2)**2)


# Ensure n is even
if n % 2 == 1:
    n += 1

# Calculate the width of each subinterval
h = (b - a) / n

# Simpson's Rule calculation
integral = f(a , q) + f(b , q)

for i in range(1, n, 2):
    integral += 4 * f(a + i * h , q)

for i in range(2, n-1, 2):
    integral += 2 * f(a + i * h , q)

integral *= h / 3

# Print the result
print(f"Approximate work done moving the conducting sphere from {a} to {b} using Simpson's Rule: {integral}")
