import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Trapezoidal integration function
def integralTrapezoidal(data):
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

yStart = [0, 0.21, 0.3, 0, 0, 0]  # Initial conditions for position and velocity

# Solve the system using Runge-Kutta (RK45) numerical integration
solution = solve_ivp(
    f_nosc, 
    [tStart, tEnd], 
    yStart, 
    args=(n, k, m, fixed_end), 
    method='RK45',  
    t_eval=np.linspace(0, 100, 1001)  # Evaluate at 1001 time points
)

list1 = list(np.linspace(0, 100, 1001))  # Time points

fig, axes = plt.subplots(1, 3, figsize=(16,6))  # Create subplots for Fourier spectra

for i in range(n):
    
    # Compute the Fourier transform of the oscillator's motion
    ft = [np.array([w, (np.real(1/np.sqrt(2*np.pi) * integralTrapezoidal(np.array([list1, solution.y[i] * np.exp(1j*w*np.linspace(0,100,1001))]))))**2]) for w in np.linspace(0,3,301)]
  
    ft = np.transpose(ft)  # Transpose for plotting
    
    axes[i].plot(ft[0], ft[1])  # Plot the Fourier transform for each oscillator
    
    axes[i].set_xlabel(f'frequency{i+1}')  # Label x-axis as frequency
    
    axes[i].set_ylabel(f'intensity{i+1}')  # Label y-axis as intensity
    
plt.savefig("fourier_spectrum_plots.png", dpi=100)  # Save the plot as a PNG file
