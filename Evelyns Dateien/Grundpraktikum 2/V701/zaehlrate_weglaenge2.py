import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show
 
 
 
x, y = np.loadtxt('zaehlrate_weglaenge2.txt', unpack=True,delimiter=',')
e, g = np.loadtxt('regression2.txt', unpack=True,delimiter=',')
 
plt.axhline(y=57.427, color='r', linestyle='dashed')

def f(e,a,b):
    return a*e+b
popt, pcov = curve_fit(f, e, g)
errors = np.sqrt(np.diag(pcov))
 
print('a =', popt[0], '±', errors[0])
print('b =', popt[1], '±', errors[1])
e_new = np.linspace(12.8, 21.25, 8) 
 
plt.figure(1)
plt.plot(x,y,'x', label ='Messwerte')
plt.plot(e_new, f(e_new,*popt),'-', label='Linearer Fit')

 
 
plt.ylabel(r'$Zählrate/\,10^{3}$')
plt.xlabel(r'$x_0 \, / \,mm$')
plt.grid()
plt.legend()
 
 
 
 
plt.savefig('zaehlrate_weglaenge2.pdf')
print ('Fertig')