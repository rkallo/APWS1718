import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show
 
 
 
x, y = np.loadtxt('energie_weglaenge2.txt', unpack=True,delimiter=',')


def f(x,a,b):
    return a*x+b
popt, pcov = curve_fit(f, x, y)
errors = np.sqrt(np.diag(pcov))
 
print('a =', popt[0], '±', errors[0])
print('b =', popt[1], '±', errors[1])
x_new = np.linspace(0, 20, 21) 
 
plt.figure(1)
plt.plot(x,y,'x', label ='Messwerte')
plt.plot(x_new, f(x_new,*popt),'-', label='Linearer Fit')
 
 
plt.ylabel(r'$E/\,10^{6}eV$') 
plt.xlabel(r'$x_0 \, / \,mm$')
plt.grid()
plt.legend()
 
 
 
 
plt.savefig('energie_weglaenge2.pdf')
print ('Fertig')