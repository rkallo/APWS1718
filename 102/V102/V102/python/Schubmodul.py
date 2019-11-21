import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import unumpy as unp
from uncertainties import ufloat
from astropy.io import ascii
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

plt.rcParams['figure.figsize'] = (10, 8)
plt.rcParams['font.size'] = 16
plt.rcParams['lines.linewidth'] = 2

N = 80
E = ufloat(210 * 10**9, 0.5 * 10**9)          # in Pascal
R = 72 * 10**-3       # Spulenradius in m
D_KH = 22.5 * 10**-7         # Trägheitsmoment Halterung in kg/m^2
R_k = ufloat(51.03*10**-3, 0.020412*10**-3) / 2       # Kugelradius in m
m_k = ufloat(588.3, 0.23532) * 10**-3                 # Kugelmasse in kg
L = (61.7 + 4.2) * 10**-2                             # Länge des Drahtes in m
I = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])      # Strom in A
Anzahl1, T = np.genfromtxt('rohdaten/Schubmodul.txt', unpack=True)
Anzahl2, d1 = np.genfromtxt('rohdaten/Drahtdurchmesser.txt', unpack=True)
Anzahl3, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10 = np.genfromtxt('rohdaten/MagnetischerMoment.txt', unpack=True)
Anzahl4, Te = np.genfromtxt('rohdaten/Erdmagnetfeld.txt', unpack=True)

# a)
print('A')
r = ufloat(np.mean(d1), np.std(d1)) / 2 * 10**-3
print('R = ', r*10**3, 'in mm')
print('RK =', R_k *10**3, 'in mm')


def G(T, R, L, d):
    return 8 * np.pi * L * d / (T**2 * R**4)


def d(mk, Rk, DK):
    return(2/5*mk*Rk**2)+DK

d_all = d(m_k, R_k, D_KH)
G_gem = G(T, r, L, d_all)
print('Gesamtträgheitsmoment =', d_all*10**3, 'in g m^2')
print('G = ', np.mean(G_gem)*10**-9, 'in GPa')
G_all = np.mean(G_gem)
P = (G_all*10**-9/81-1)*100
print('Fehler von G =', P)
ascii.write([T, np.round(noms(G_gem)*10**-9, 2), np.round(stds(G_gem)*10**-9, 2)], 'build/Schubmodul.tex', format='latex', names=['$T/\si{\second}$', 'nix', '$G/\si{\giga\pascal}$'])
mu = E/(2*G_all)-1
Q = E*G_all/(9*G_all - 3*E)
print('\mu = ', mu, 'Einheitenlos')
print('Q =', Q*10**-12, 'in TPa')

# b1)
print('B1')


def B(I, N, R):
    return 4 * np.pi * 10**-7 * 8 * I * N / (np.sqrt(125) * R)


def f(x, a, b):
    return a * x + b


def D(G, R, L):
    return np.pi * G * R**4 / (2 * L)


def m(T, d, B, D):
    return 4 * np.pi**2 * d / (B * T**2) - D/B

D_all = D(np.mean(G_gem), r, L)
T_mean = np.array([np.mean(T1), np.mean(T2), np.mean(T3), np.mean(T4), np.mean(T5), np.mean(T6), np.mean(T7), np.mean(T8), np.mean(T9), np.mean(T10)])
T_std = np.array([np.std(T1), np.std(T2), np.std(T3), np.std(T4), np.std(T5), np.std(T6), np.std(T7), np.std(T8), np.std(T9), np.std(T10)])
Ta = unp.uarray(T_mean, T_std)
z = 1/(T_mean**2)
params1, covariance1 = curve_fit(f, z, B(I, N, R))
errors1 = np.sqrt(np.diag(covariance1))
print('a1 =', params1[0], '±', errors1[0], 'in kg/A')
print('b1 =', params1[1], '±', errors1[1], 'in T')
T_plot = np.linspace(8.8, 19)
plt.plot(1/(T_mean**2)*10**3, B(I, N, R)*10**3, 'rx', label='Messwerte')
plt.plot(1/(T_plot**2)*10**3, f(1/(T_plot**2), *params1)*10**3, 'b-', label='Regression')
plt.ylabel(r'$B / \mathrm{mT}$')
plt.xlabel(r'$\frac{1}{T^2} / \frac{\mathrm{m}}{\mathrm{s}^2}$')
plt.legend(loc='best')
plt.savefig('build/TB-Diagramm.pdf')
a = ufloat(params1[0], errors1[0])
m1 = (4 * np.pi**2 * d_all)/a
print('m aus der Regression =', m1, 'in A m^2')

m2 = m(T_mean, d_all, B(I, N, R), D_all)
print('m aus den Messwerten =', np.mean(m2), 'in A m^2')
Anzahl = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
ascii.write([T1, T2, T3, T4, T5, T6, T7, T8, T9, T10], 'build/MagnetischerMoment1.tex', format='latex', names=['$T_{0.1}/\si{\second}$', '$T_{0.2}/\si{\second}$', '$T_{0.3}/\si{\second}$', '$T_{0.4}/\si{\second}$', '$T_{0.5}/\si{\second}$', '$T_{0.6}/\si{\second}$', '$T_{0.7}/\si{\second}$', '$T_{0.8}/\si{\second}$', '$T_{0.9}/\si{\second}$', '$T_{1.0}/\si{\second}$', ])
ascii.write([Anzahl*10**-1, np.round(noms(Ta), 2), np.round(stds(Ta), 2), np.round(noms(1/Ta**2*10**3), 2), np.round(stds(1/Ta**2*10**3), 2), I, np.round(B(I, N, R)*10**3, 2)], 'build/MagnetischerMoment2.tex', format='latex', names=['Index', '$\\bar{T}_\\text{i}/\si{\second}$', 'nix', '$\\frac{1}{\\bar{T}_\\text{i}^2}/\si{\mili\per\second\square}$', 'nix2', '$I_\\text{i}/\si{\\ampere}$', '$B/\si{\mili\\tesla}$'])

# c)
print('C')


def B2(d, T, m, D):
    return 4 * np.pi**2 * d / (T**2 * m) - D/m

BE = B2(d_all, Te, m1, D_all)
print('Erdmagnetfeld =', np.mean(BE)*10**6, 'in mücro T')
print('Fehler BE =', (np.mean(BE*10**6)/20-1)*100)
ascii.write([Te, np.round(1/Te**2*10**3, 2), np.round(noms(BE*10**3), 2), np.round(stds(BE*10**3), 2)], 'build/Erdmagnetfeld.tex', format='latex', names=['$T/\si{\second}$', '$\\frac{1}{T^2}/\si{\mili\per\second\squared}$', '$B/\si{\mili\\tesla}$', 'nix'])
