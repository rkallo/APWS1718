import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show
 
 
 
x, y = np.loadtxt('FrequenzSpannung_linear.txt', unpack=True,delimiter=',')
 
plt.axhline(y=2.665085458, color='r', linestyle='dashed')
 
 
plt.figure(1)
plt.plot(x,y,'x', label ='Messwerte')
 
 
plt.ylabel(r'$\frac{U_c}{U_0}$')
plt.xlabel(r'$\nu \, / \, 10^{3}\, Hz$')
plt.grid()
plt.legend()
 
 
 
 
plt.savefig('FrequenzSpannung_linear.pdf')
print ('Fertig')