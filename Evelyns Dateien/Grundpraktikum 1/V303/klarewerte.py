import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show
 
 
 
x, y = np.loadtxt('klarewerte.txt', unpack=True,delimiter=',')
 

 
 
 
plt.figure(1)
plt.plot(x,y,'x', label ='Messwerte')
 
 
plt.ylabel('$U [mV]$')
plt.xlabel('$\phi [Grad]$')
plt.grid()
plt.legend()
 
 
 
 
plt.savefig('klarewerte.pdf')
print ('Fertig')