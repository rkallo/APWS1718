import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

x, y = np.loadtxt('Kurve1.txt', unpack=True, delimiter=',')

def f(x,a,b):
    return a*x+b
popt, pcov = curve_fit(f, x, y)

errors = np.sqrt(np.diag(pcov))
print('a =', popt[0], '±', errors[0])
print('b =', popt[1], '±', errors[1])

x_new = np.linspace(0.00000241230 , 0.00000610700, 1000)

plt.figure(1)
plt.plot(x, y,'rx')
plt.plot(x_new, f(x_new,*popt),'-', label='Linearer Fit')

plt.ylabel('$n^2$')
plt.xlabel('$\lambda^-2$ / $10^-6 1/(nm)^2$')
plt.grid()
plt.legend(loc='best')


plt.savefig('Kurve1.pdf')
