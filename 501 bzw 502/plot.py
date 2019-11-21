import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('Leuchtpunktverschiebung1')

x, y = np.loadtxt('Leuchtpunktverschiebung1.txt', unpack=True,delimiter=',')

def f(x,a,b):
    return a*x+b
popt, pcov = curve_fit(f, x, y)
print(popt)
print(pcov)

x_new = np.linspace(-23 , 12 , 1000)
#xyab

print('Leuchtpunktverschiebung2')

z, u = np.loadtxt('Leuchtpunktverschiebung2.txt', unpack=True,delimiter=',')

def f(z,e,f):
    return e*z+f
popt2, pcov2 = curve_fit(f, z, u)
print(popt2)
print(pcov2)

z_new = np.linspace(-35 , 13 , 1000)
#zuef
print('Leuchtpunktverschiebung3')

q, t = np.loadtxt('Leuchtpunktverschiebung3.txt', unpack=True,delimiter=',')

def f(q,w,r):
    return w*q+r
popt3, pcov3 = curve_fit(f, q, t)
print(popt3)
print(pcov3)

q_new = np.linspace(-35 , 17 , 1000)
#qtwr

print('Leuchtpunktverschiebung4')

i, o = np.loadtxt('Leuchtpunktverschiebung4.txt', unpack=True,delimiter=',')

def f(i,p,v):
    return p*i+v
popt4, pcov4 = curve_fit(f, i, o)
print(popt4)
print(pcov4)

i_new = np.linspace(-30 , 18 , 1000)


#xyab
#zuef
#qtwr
#iopv

print('Leuchtpunktverschiebung5')

s, d = np.loadtxt('Leuchtpunktverschiebung5.txt', unpack=True,delimiter=',')

def f(s,g,h):
    return g*s+h
popt5, pcov5 = curve_fit(f, s, d)
print(popt5)
print(pcov5)

s_new = np.linspace(-30 , 20 , 1000)

plt.figure(1)
plt.plot(x,y,'x')
plt.plot(z,u,'x')
plt.plot(q,t,'x')
plt.plot(i,o,'x')
plt.plot(s,d,'x')
plt.plot(x_new,f(x_new,*popt),'-', label='$220V$')
plt.plot(z_new,f(z_new,*popt2),'-',label='$300V$')
plt.plot(q_new,f(q_new,*popt3),'-', label='$350V$')
plt.plot(i_new,f(i_new,*popt4),'-', label='$420V$')
plt.plot(s_new,f(s_new,*popt5),'-', label='$450V$')

plt.ylabel('$D$ / $cm$')
plt.xlabel('$U_{d}$ / $V$')
plt.grid()
plt.legend()


plt.savefig('V501.pdf')
