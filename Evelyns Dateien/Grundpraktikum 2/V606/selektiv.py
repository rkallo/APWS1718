import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show
from fractions import * 
 
 
 
x, y = np.loadtxt('selektiv.txt', unpack=True,delimiter=',')
 
 


 
plt.figure(1)
plt.plot(x, y,'rx', label='Messdaten')


 
plt.ylabel('$U$ $/ \, V$')
plt.xlabel(r'$\nu$ $/ 10^{3}\, Hz$')
plt.grid()
plt.legend()
 
 
plt.savefig('selektiv.pdf')
print ('Fertig')