import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show
 
 
 
x, y = np.loadtxt('halbwertsbreite.txt', unpack=True,delimiter=',')
 
 
 
 
plt.axhline(y=2.628315906, color='r', linestyle='-')
 

 
 
 
plt.figure(1)
plt.plot(x,y,'x', label ='Messwerte')
 
 
plt.ylabel('$U_c [V]$')
plt.xlabel('$t [s]$')
plt.grid()
plt.legend()
 
 
 
 
plt.savefig('Halbwertsbreite.pdf')
print ('Fertig')