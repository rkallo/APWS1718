import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unpack
from uncertainties import ufloat
from scipy.stats import stats
import pylab

U = 5
x , y = np.loadtxt('Freq.txt' , unpack = True, delimiter=',')
y = y/U
x_new = np.linspace(10, 10000, 100000)

def f(x, a):
    return 1/np.sqrt(1+(2*np.pi*x*a)**2)
popt, pcov = curve_fit(f, x, y)
print(popt)
print(pcov)

plt.figure(1)

errors = np.sqrt(np.diag(pcov))

print('a =', popt[0], '±', errors[0])
#print('b =', popt[1], '±', errors[1])

plt.plot(x,y,'x', label ='Messwerte')
plt.plot(x_new,f(x_new,*popt),'-', label='Ausgleichsrechnug')
plt.xscale('log')

plt.ylabel('$[U_c] V $')
plt.xlabel('$[f] Hz$')
plt.grid()
plt.legend(loc="best")

plt.savefig('Freq.pdf')
