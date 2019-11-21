import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show
 
 
x, y = np.loadtxt('beidseitig_links.txt', unpack=True,delimiter=',')
 
 
def f(x,a,b):
    return a*x+b
popt, pcov = curve_fit(f, x, y)
errors = np.sqrt(np.diag(pcov))
 
print('a =', popt[0], '±', errors[0])
print('b =', popt[1], '±', errors[1])

x_new = np.linspace(80, 211, 10)
 
plt.figure(1)
plt.plot(x, y,'rx', label='Messdaten')
plt.plot(x_new, f(x_new,*popt),'-', label='Linearer Fit')
 
plt.ylabel('$D(x)$ $[10^{-3} m]$')
plt.xlabel(r'$(4x^3 - 12Lx^2 + 9L^2x - L^3)$ $\left[10^{-3} m^3\right]$')
plt.grid()
plt.legend(loc='best')
 
 
plt.savefig('beidseitig_links.pdf')