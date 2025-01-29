import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def integral(data):
    a = 0
    for i in range(len(data[0])-1):
        a = a + (data[0,i+1] -data[0,i]) * (data[1,i+1] + data[1,i]) / 2
        
    return a



def f_nosc(t, y, n, k, m, fixed_end):
    
    r = y[0:n]
    v = y[n:2*n]
    eqs = []
    
    if fixed_end is True :
        for i in range(n):
            if i == 0:
                eq = -k/m*(2*r[i] -r[i+1])
            elif i == n-1:
                eq = -k/m*(2*r[i] -r[i-1])
            else:
                eq = -k/m*(2*r[i] -r[i-1] -r[i+1])
            eqs.append(eq)
    else :
        for i in range(n):
            if i == 0:
                eq = -k/m*(r[i] -r[i+1])
            elif i == n-1:
                eq = -k/m*(r[i] -r[i-1])
            else:
                eq = -k/m*(2*r[i] -r[i-1] -r[i+1])
            eqs.append(eq)
    
    return list(v) + eqs

fixed_end = True

n = 3
k = 1
m = 1

tStart = 0
tEnd = 100

yStart = [0, 0.17, 0.3, 0, 0, 0]

solution = solve_ivp(
    f_nosc, 
    [tStart,tEnd], 
    yStart, 
    args=(n,k,m,fixed_end), 
    method = 'RK45', 
    t_eval = np.linspace(0,100,1001)
)

list1 = list(np.linspace(0,100,1001))

ft = [np.array([w, (np.real(1/np.sqrt(2*np.pi)*integral(np.array([list1, solution.y[0]*np.exp(1j*w*np.linspace(0,100,1001))]))))**2]) for w in np.linspace(0,3,301)]

ft = np.transpose(ft)

plt.plot(ft[0], ft[1])
plt.xlabel('frequency')
plt.ylabel('FT intensity')
