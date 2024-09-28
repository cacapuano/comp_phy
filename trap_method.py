#Work done to move a conducting sphere using the electric field. Integrate using the trapezodial rule

import numpy as np
import matplotlib.pyplot as plt

#constants
e_0 = 8.85e-12 #C^2/Nm^2 permittivity of free space
q = 1e-6 # coulombs - charge of the conducting sphere
R = 3e-3 # m radius of the sphere 

#integration parameters
a = R #lower limit of integration
b = 3 # m upper limit of integration
intervals = 1000 #steps

# defining function to integrate
def work(r):
    e_0 = 8.85e-12
    top = e_0/2
    k = 1 / (4 * np.pi * e_0)
    E_field = (k * q / r**2)**2
    return top * E_field


# trapezoidal rule method of integration
def trapezoidal_rule(function, a, b, intervals):
    h = (b-a)/intervals #width of interval
    integral = 0.5 * (function(a) + function(b))
    
    for i in range(1, intervals):
        integral += function(a + i * h)
    
    integral *= h
    return integral


# integrate using the trapezoidal rule
Work_integrated_trap = trapezoidal_rule(work, a, b, intervals)

# print answer
print(f"Work done to move the conducting sphere from {a} m to {b} m using the Trapezoidal Method: {Work_integrated_trap:e} N*m/C")

