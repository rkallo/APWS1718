
import numpy as np
import sympy as sy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('Alle')

v, s, t = np.loadtxt('alu_fehler.txt', unpack=True,delimiter=',')






print('Ausgleichsgerade Absorptionskurve')

z, u, n = np.loadtxt('alu_fehler1.txt', unpack=True,delimiter=',')
R=np.log(n)

plt.errorbar(z, u, yerr=R, fmt="none", capsize=5, capthick=2, ms=9, markerfacecolor="r")

def q(z,e,w):
    return e*z+w
popt2, pcov2 = curve_fit(q, z, u)
print(popt2)
print(pcov2)

z_new = np.linspace(0, 0.08, 7)






print('Ausgleichsgerade Hintergrundsstrahlung')

x, y, m = np.loadtxt('alu_fehler2.txt', unpack=True,delimiter=',')
T=np.log(m)

plt.plot(x, y, "xg", label="Ausgleichsgerade Hintergrundsstrahlung")
plt.errorbar(x, y, yerr=T , fmt="none", capsize=5, capthick=2, ms=9)

def f(x,a,b):
    return a*x+b
popt, pcov = curve_fit(f, x, y)
print(popt)
print(pcov)

x_new = np.linspace(0.07, 0.13, 5)







plt.figure(1)
plt.plot(v, s,'rx', label='Messdaten')
plt.plot(z_new,q(z_new,*popt2),'-',label='Ausgleichsgerade Absorptionskurve')
plt.plot(x_new,f(x_new,*popt),'-', label='Ausgleichsgerade Hintergrundsstrahlung')

plt.xlabel('Massenbelegung R')
plt.ylabel('ln(Z-Zu)')
plt.grid()
plt.legend()



plt.savefig('alu.pdf')
print ('Fertig')
