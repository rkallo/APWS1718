import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show
from fractions import * 
 
 
 
x, y = np.loadtxt('orangePhoto.txt', unpack=True,delimiter=',')
 
 


 
plt.figure(1)
plt.plot(x, y,'rx', label='Messdaten')


 
plt.ylabel('$I$ $/ \, 10^{-9} A$')
plt.xlabel(r'$U$ $/ \, V$')
plt.grid()
plt.legend()
 
 
plt.savefig('orangePhoto.pdf')
print ('Fertig')