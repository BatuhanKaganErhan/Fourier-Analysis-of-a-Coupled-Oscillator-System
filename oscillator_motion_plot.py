import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Trapezoidal integration function
def integral(data):
    a = 0
    for i in range(len(data[0])-1):
        # Apply the trapezoidal rule for numerical integration
        a = a + (data[0,i+1] - data[0,i]) * (data[1,i+1] + data[1,i]) / 2
    return a

# Function defining the system of differential equations for coupled oscillators
def f_nosc(t, y, n, k, m, fixed_end):
    
    r = y[0:n]  # Position components
    v = y[n:2*n]  # Velocity components
    eqs = []  # List to store the differential equations
    
    if fixed_end is True:
        # If the ends are fixed, apply boundary conditions accordingly
        for i in range(n):
            if i == 0:
                eq = -k/m * (2 * r[i] - r[i+1])
            elif i == n-1:
                eq = -k/m * (2 * r[i] - r[i-1])
            else:
                eq = -k/m * (2 * r[i] - r[i-1] - r[i+1])
            eqs.append(eq)
    else:
        # If the ends are free, apply a different set of boundary conditions
        for i in range(n):
            if i == 0:
                eq = -k/m * (r[i] - r[i+1])
            elif i == n-1:
                eq = -k/m * (r[i] - r[i-1])
            else:
                eq = -k/m * (2 * r[i] - r[i-1] - r[i+1])
            eqs.append(eq)
    
    return list(v) + eqs  # Return velocity and acceleration components

fixed_end = True  # Define whether the system has fixed ends

n = 3  # Number of oscillators
k = 1  # Spring constant
m = 1  # Mass of each oscillator

tStart = 0  # Start time
tEnd = 100  # End time

yStart = [0, 0.17, 0.3, 0, 0, 0]  # Initial conditions for position and velocity

# Solve the system using Runge-Kutta (RK45) numerical integration
solution = solve_ivp(
    f_nosc, 
    [tStart, tEnd], 
    yStart, 
    args=(n, k, m, fixed_end), 
    method='RK45',  
    t_eval=np.linspace(0, 100, 1001)  # Evaluate at 1001 time points
)

# Plot the position of each oscillator over time with vertical offset for clarity
for i in range(n):
    plt.plot(solution.t, solution.y[i] + (i+1))  # Shift each plot vertically by (i+1) to separate them
