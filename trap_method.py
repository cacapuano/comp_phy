#Work done to move a conducting sphere using the electric field. Integrate using the trapezodial rule

import numpy as np
import matplotlib.pyplot as plt

#constants
e_0 = 8.85e-12 #C^2/Nm^2 permittivity of free space
q = 1e-6 # coulombs - charge of the conducting sphere
r = 3e-3 # radius of the sphere m

#integration parameters
a = 1 #lower limit of integration
b = 10 #upper limit of integration
intervals = 1000 #steps

#work done moving conducting sphere integral
def work(r,q):
    e_0 = 8.85e-12
    return (e_0/2)((1 / (4 * np.pi * e_0)) * (q / r**2)**2)
work(r,q)

#trapezoidal rule method
def trapezoidal_rule(f, a, b, n, q):
    h = (b-a)/n #width of interval
    integral = 0.5 * (work(a, q) + work(b, q))

    for i in range(1 , n):
        x_i = a + i * h
        integral += work(x_i , q)
    
    integral *= h
    return integral
trapezoidal_rule(f, a, b, n, q)

print(f"Work done to move the conducting sphere: {integral} J")



