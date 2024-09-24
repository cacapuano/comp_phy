#Work done to move a conducting sphere using the electric field. Integrate using the trapezodial rule

import numpy as np
import matplotlib.pyplot as plt

#constants
e_0 = 
q = 
r = 

#integration parameters
a = 0 #lower limit of integration
b = 10 #upper limit of integration
intervals = 1000 #steps

#work done moving conducting sphere integral
def work(r,q):
    epislon_0 = 8.85e-12
    return (epsilon_0/2)((1 / (4 * np.pi * epsilon_0)) * (q / r**2)**2)

#trapezoidal rule method
def trapezoidal_rule(f, a, b, n, q):
    h = (b-a)/n #width of interval
    integral = 0.5 * (f(a, Q) + f(b, Q))

    for i in range(1 , n):
        x_i = a + i * h
        integral += f(x_i , q)
    
    integral *= h
    return integral

#simpson's method
def simpsons_method():



