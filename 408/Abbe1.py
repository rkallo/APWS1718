import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

x, y = np.loadtxt('Abbe1.txt', unpack=True, delimiter=',')

def f(x,a,b):
    return a*x+b
popt, pcov = curve_fit(f, x, y)

errors = np.sqrt(np.diag(pcov))
print('a =', popt[0], '±', errors[0])
print('b =', popt[1], '±', errors[1])

x_new = np.linspace(1.45 , 3.25 , 100)

plt.figure(1)
plt.plot(x, y,'rx')
plt.plot(x_new, f(x_new,*popt),'-', label='Linearer Fit')

plt.ylabel('$g / m$')
plt.xlabel('$1+1/V$')
plt.grid()
plt.legend(loc='best')


plt.savefig('Abbe1.pdf')
