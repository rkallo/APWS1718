import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show


x, y = np.loadtxt('Zeit.txt', unpack=True , delimiter=',')

def f(x,a,b):
    return a*x+b
popt, pcov = curve_fit(f, x, y)
print(popt)
print(pcov)

errors = np.sqrt(np.diag(pcov))

print('a =', popt[0], '±', errors[0])
print('b =', popt[1], '±', errors[1])


x_new = np.linspace(x[0] , x[27] , 30)

plt.figure(1)
plt.plot(x, y ,'x', label ='Messwerte')
plt.plot(x_new, f(x_new,*popt),'-', label='Lineare Regression')


plt.ylabel('$ln({U_c})$')
plt.xlabel('$[t]/ms$')
plt.grid()
plt.legend()


plt.savefig('Zeit.pdf')
print ('Fertig')
