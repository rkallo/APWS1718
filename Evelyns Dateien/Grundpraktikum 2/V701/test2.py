import matplotlib.pyplot as plt
from numpy.random import normal, uniform
import numpy as np
import math
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show
 

N = np.loadtxt('statistik.txt', unpack=True,delimiter=',')
sg = np.random.normal(N)


plt.hist(sg, bins=43, histtype='stepfilled', normed=True, facecolor='g', label='Gaussian')
plt.hist(N, bins=26, histtype='stepfilled', normed=True, facecolor='b', alpha=0.6, label='Histogram')


plt.title("Gaussian/Uniform Histogram")
plt.xlabel("Value")
plt.ylabel("Probability")

plt.legend()
plt.savefig('test2.pdf')
print ('Fertig')