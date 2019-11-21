import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show


x, y = np.loadtxt('Abstand3.txt', unpack=True,delimiter=',')

x_new = np.linspace(0.8 , 20 , 100)

plt.figure(1)
plt.plot(x, y,'rx', label='Messdaten')

plt.ylabel(r'$B / \mathrm {mT}$')
plt.xlabel(r'$x / \mathrm{cm}$')
plt.grid()
plt.legend(loc='best')


plt.savefig('Abstand3.pdf')
