#using SciPy to integrate work moving a conducting sphere

from scipy.integrate import quad
import numpy as np

def integrand(r, a, b):
    epislon_0 = 8.85e-12
    return (epsilon_0/2)((1 / (4 * np.pi * epsilon_0)) * (q / r**2)**2)


I = quad(integrand, 1, 10, args=())
