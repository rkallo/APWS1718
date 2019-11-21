import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

# Dateien laden, speichern in x1 und y1, x2 und y2 usw
x1, y1 = np.loadtxt('1a.txt', unpack=True, delimiter=',')
x2, y2 = np.loadtxt('2a.txt', unpack=True, delimiter=',')
x3, y3 = np.loadtxt('3a.txt', unpack=True, delimiter=',')
x4, y4 = np.loadtxt('4a.txt', unpack=True, delimiter=',')
x5, y5 = np.loadtxt('5a.txt', unpack=True, delimiter=',')
x6, y6 = np.loadtxt('6a.txt', unpack=True, delimiter=',')
x7, y7 = np.loadtxt('7a.txt', unpack=True, delimiter=',')
x8, y8 = np.loadtxt('8a.txt', unpack=True, delimiter=',')
x9, y9 = np.loadtxt('9a.txt', unpack=True, delimiter=',')
x10, y10 = np.loadtxt('10a.txt', unpack=True, delimiter=',')

# Fit Funktion einmal definieren
def f(x,a,b):
    return a*x+b

# Fitten, Ergebnis jeweils in andere Variable speichern
popt1, pcov1 = curve_fit(f, x1, y1)
popt2, pcov2 = curve_fit(f, x2, y2)
popt3, pcov3 = curve_fit(f, x3, y3)
popt4, pcov4 = curve_fit(f, x4, y4)
popt5, pcov5 = curve_fit(f, x5, y5)
popt6, pcov6 = curve_fit(f, x6, y6)
popt7, pcov7 = curve_fit(f, x7, y7)
popt8, pcov8 = curve_fit(f, x8, y8)
popt9, pcov9 = curve_fit(f, x9, y9)
popt10, pcov10 = curve_fit(f, x10, y10)

# Fehler berechnen (gibt hier Fehlermeldung weils keine Fehler gibt!)
errors1 = np.sqrt(np.diag(pcov1))
errors2 = np.sqrt(np.diag(pcov2))
errors3 = np.sqrt(np.diag(pcov3))
errors4 = np.sqrt(np.diag(pcov4))
errors5 = np.sqrt(np.diag(pcov5))
errors6 = np.sqrt(np.diag(pcov6))
errors7 = np.sqrt(np.diag(pcov7))
errors8 = np.sqrt(np.diag(pcov8))
errors9 = np.sqrt(np.diag(pcov9))
errors10 = np.sqrt(np.diag(pcov10))

# Fehler nicht ausgeben weil es keine gibt. Nur 2 Punkte zum fitten -> kein Fehler
#print('a =', popt1[0], '±', errors1[0])
#print('b =', popt1[1], '±', errors1[1])
print('a =', popt1[0])
print('b =', popt1[1])

# x-Werte zum plotten definieren, 1000 zwischen 0 und 0.51
x_new = np.linspace(-0.5, 0.5, 1000)

# plotten
plt.figure(1)
#plt.plot(x1, y1, 'rx')
#plt.plot(x2, y2, 'rx')
#plt.plot(x3, y3, 'rx')
#plt.plot(x4, y4, 'rx')
#plt.plot(x5, y5, 'rx')
plt.plot(x_new, f(x_new,*popt1),'-', label='Linearer Fit 1')
plt.plot(x_new, f(x_new,*popt2),'-', label='Linearer Fit 2')
plt.plot(x_new, f(x_new,*popt3),'-', label='Linearer Fit 3')
plt.plot(x_new, f(x_new,*popt4),'-', label='Linearer Fit 4')
plt.plot(x_new, f(x_new,*popt5),'-', label='Linearer Fit 5')
plt.plot(x_new, f(x_new,*popt6),'-', label='Linearer Fit 6')
plt.plot(x_new, f(x_new,*popt7),'-', label='Linearer Fit 7')
plt.plot(x_new, f(x_new,*popt8),'-', label='Linearer Fit 8')
plt.plot(x_new, f(x_new,*popt9),'-', label='Linearer Fit 9')
plt.plot(x_new, f(x_new,*popt10),'-', label='Linearer Fit 10')

plt.ylabel('$b / m$')
plt.xlabel('$g /m$')
plt.grid()
plt.legend(loc='best')


plt.savefig('Messungen2.pdf')
