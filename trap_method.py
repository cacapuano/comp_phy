#Work done to move a conducting sphere using the electric field. Integrate using the trapezodial rule

import numpy as np
import matplotlib.pyplot as plt

#constants
e_0 = 8.85e-12 #C^2/Nm^2 permittivity of free space
q = 1e-6 # coulombs - charge of the conducting sphere
R = 3e-3 # radius of the sphere m

#integration parameters
a = 1 #lower limit of integration
b = 3 #upper limit of integration
intervals = 1000 #steps

#work done moving conducting sphere integral
def work(r):
    e_0 = 8.85e-12
    top = e_0/2
    k = 1 / (4 * np.pi * e_0)
    E_field = (k * q / r**2)**2
    return top * E_field
#work(r)

#trapezoidal rule method
def trapezoidal_rule(function, a, b, intervals):
    h = (b-a)/intervals #width of interval
    #integral = 0.5 * (work(a, q) + work(b, q))
    integral = 0.5 * (function(a) + function(b))
    #for i in range(1 , intervals):
     #   x_i = a + i * h
      #  integral += work(x_i , q)
    for i in range(1, intervals):
        integral += function(a + i * h)
    integral *= h
    return integral
#trapezoidal_rule(a, b, intervals, q)
#trapezoidal_rule(integral)

#print(f"Work done to move the conducting sphere: {integral} J")

# Integrate using the trapezoidal rule
Work_integrated = trapezoidal_rule(work, a, b, intervals)

# Range of r values for plotting
r_values = np.linspace(0.05, 0.5, 100)
Work_values = [work(r) for r in r_values]

print(f"Work done to move the conducting sphere from {R} m to {b} m: {Work_integrated:e} N*m/C")

