import matplotlib.pyplot as plt
from numpy.random import normal, uniform
import numpy as np
import math
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show
 

N = np.loadtxt('statistik.txt', unpack=True,delimiter=',')
sg = np.random.normal(N)
mu = np.random.poisson(N)


plt.hist(mu, bins=43, histtype='stepfilled', normed=True, facecolor='r',    label='Poisson-Verteilung')
plt.hist(sg, bins=85, histtype='stepfilled', normed=True, facecolor='g', label='Gauß-Verteilung')
plt.hist(N, bins=26, histtype='stepfilled', normed=True, facecolor='b', alpha=0.6, label='Messwerte')


plt.xlabel("Zählrate")
plt.ylabel("Wahrscheinlichkeit")

plt.legend()
plt.savefig('test3.pdf')
print ('Fertig')