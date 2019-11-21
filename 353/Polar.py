import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show
from scipy.stats import linregress

a, b, U = np.loadtxt('Polar.txt', unpack=True, delimiter=',')

def H(x, c):
    return -np.sin(c)/x
phi = a/b*2*np.pi
A = U/5.21
plt.figure(2)
plt.polar(phi, A, 'rx', label="Messwerte")
x = np.linspace( 2 , 0.0000001 , 100)
plt.polar(x, H(-np.tan(x), x), label= "Theoriekurve")
plt.grid()
plt.grid()
plt.savefig('Polar.pdf')
print ('Fertig')
