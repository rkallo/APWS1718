import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show
from fractions import * 
 
 
 
x, y = np.loadtxt('einzelspalt_b.txt', unpack=True,delimiter=',')


 
plt.figure(1)
plt.plot(x, y,'rx', label='Messdaten')



 
plt.ylabel(r'$Strömungsgeschwindigkeit\,\,v$ $/ \, \frac{m}{s} $')
plt.xlabel(r'$Messtiefe\,\,x$ $/ \, \mu s$')
plt.grid()
plt.legend()
 
 
plt.savefig('einzelspalt_b.pdf')
print ('Fertig')