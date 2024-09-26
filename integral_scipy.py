#using SciPy to integrate work moving a conducting sphere

from scipy.integrate import quad
import numpy as np

#constants
e_0 = 8.85e-12 #C^2/Nm^2 permittivity of free space
q = 1e-6 # coulombs - charge of the conducting sphere
R = 3e-3 # radius of the sphere m
a = R #start integration at the radius of the sphere
b = 3 # m

# defining function that we will be integrating over to find the work done
def work(r):
    if r < R:
        return 0 # electric field will be zero inside sphere
    e_0 = 8.85e-12
    top = e_0/2
    k = 1 / (4 * np.pi * e_0)
    E_field = (k * q / r**2)**2
    return top * E_field


# integrate function
Work_integrated_SciPy, error = quad(work, a, b)

print(f"Work done to move the conducting sphere from {R} m to {b} m using SciPy: {Work_integrated_SciPy:e} N*m/C")

