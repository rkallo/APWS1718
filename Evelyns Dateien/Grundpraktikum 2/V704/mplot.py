
import numpy as np
import sympy as sy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('Eisen')

x, y, m = np.loadtxt('gammaeisen.txt', unpack=True,delimiter=',')
T=np.log(m)

plt.plot(x, y, "xg", label="Eisen")
plt.errorbar(x, y, yerr=T , fmt="none", capsize=5, capthick=2, ms=9)

def f(x,a,b):
    return a*x+b
popt, pcov = curve_fit(f, x, y)
print(popt)
print(pcov)

x_new = np.linspace(x[0], x[-1], 500)





print('Blei')

z, u, n = np.loadtxt('gammablei.txt', unpack=True,delimiter=',')
R=np.log(n)

plt.plot(z, u, 'xr', label="Blei")
plt.errorbar(z, u, yerr=R, fmt="none", capsize=5, capthick=2, ms=9, markerfacecolor="r")

def q(z,e,w):
    return e*z+w
popt2, pcov2 = curve_fit(q, z, u)
print(popt2)
print(pcov2)

z_new = np.linspace(z[0], z[-1], 500)



plt.figure(1)
#plt.plot(x,y,'x')
#plt.plot(z,u,'x')
plt.plot(x_new,f(x_new,*popt),'-', label='Eisen')
plt.plot(z_new,q(z_new,*popt2),'-',label='Blei')

plt.xlabel('d/cm')
plt.ylabel('ln(Z-Zu)')
plt.grid()
plt.legend()



plt.savefig('Graphik1.pdf')
print ('Fertig')
