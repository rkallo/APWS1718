import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show
from fractions import * 
 
 
 
x, y = np.loadtxt('graph1.txt', unpack=True,delimiter=',')
a, b = np.loadtxt('graph2.txt', unpack=True,delimiter=',')
c, d = np.loadtxt('graph3.txt', unpack=True,delimiter=',')
 
 


 
plt.figure(1)
plt.plot(x, y,'rx', label='Messdaten für $\Theta = 15°$')
plt.plot(a, b,'bx', label='Messdaten für $\Theta = 30°$')
plt.plot(c, d,'gx', label='Messdaten für $\Theta = 60°$')


 
plt.ylabel(r'$\frac{ | \Delta \nu | }{cos(\alpha)}$ $/ \, Hz $')
plt.xlabel(r'$v$ $/ \, \frac{m}{s}$')
plt.grid()
plt.legend()
 
 
plt.savefig('graph1.pdf')
print ('Fertig')