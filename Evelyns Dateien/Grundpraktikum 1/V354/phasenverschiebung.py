import numpy as np
import matplotlib.ticker as tck
import matplotlib.pyplot as plt
import math
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show
 
 
 
x, y = np.loadtxt('phasenverschiebung.txt', unpack=True,delimiter=',')

plt.axvline(x=30, color='r', linestyle='dashed', linewidth=0.9)
plt.axvline(x=38, color='r', linestyle='dashed', linewidth=0.9)
plt.axvline(x=35, color='b', linestyle='-.', linewidth=0.9)

 
 
plt.figure(1)
plt.plot(x,y,'x', label ='Messwerte')
 
 
plt.ylabel(r'$\varphi \, / \, rad$')
plt.xlabel(r'$\nu \, / \, 10^{3} \, Hz$')
plt.grid()
plt.legend()
 
 
 
 
plt.savefig('phasenverschiebung.pdf')
print ('Fertig')


import matplotlib.ticker as tck
import matplotlib.pyplot as plt
import numpy as np