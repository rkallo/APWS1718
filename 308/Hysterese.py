import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show


x, y = np.loadtxt('Hysterese.txt', unpack=True,delimiter=',')

x_new = np.linspace(3 , -0.5 , 100)

plt.figure(1)
plt.plot(x, y,'rx', label='Messdaten')

plt.ylabel(r'$B / \mathrm {mT}$')
plt.xlabel(r'$I / \mathrm{A}$')
plt.grid()
plt.legend(loc='best')


plt.savefig('Hysterese.pdf')
