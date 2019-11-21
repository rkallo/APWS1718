import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties.unumpy as unpack
from uncertainties import ufloat
from scipy.stats import stats
import pylab

x, a, b = np.loadtxt('Freq2.txt', unpack=True,delimiter=',')
y = a/b*2*np.pi

def f(x,c):
    return np.arctan(-2*np.pi*x*c)
popt, pcov = curve_fit(f, x, y)
print(popt)
print(pcov)

errors = np.sqrt(np.diag(pcov))

print('a =', popt[0], '±', errors[0])
#print('b =', popt[1], '±', errors[1])

x_new = np.linspace(10, 10000, 100000)

plt.figure(1)
plt.plot(x,y,'x', label ='Messwerte')
plt.plot(x_new,f(x_new,*popt),'-', label='Lineare Regression')
plt.xscale('log')

plt.ylabel('$\Delta\phi/\mathrm{rad}$')
plt.xlabel('$[f]/Hz$')
plt.grid()
plt.legend(loc="best")
plt.savefig('Freq2.pdf')
print ('Fertig')
