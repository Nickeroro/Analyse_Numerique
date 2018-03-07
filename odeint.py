from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt



def dyn_ode (x, t):
    return dyn_d_avant(t, x)

h = 0.001
tmax = 10
T =np.arange (0, tmax, h)
x0 = np.array([1, 1])
solution = odeint(dyn_ode, x0, T)

plt.plot (T, solution)

