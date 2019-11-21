import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp

# txt Datei mit Ergebnissen

text_file = open("build/values.txt", "w")

# Daten einlesen

data_Schubmodul = np.genfromtxt('data/data_Schubmodul.txt', unpack=False) # [0] = Schwingungsdauer T/s, [1] = Drahtdurchmesser D/mm
data_L = np.genfromtxt('data/data_L.txt', unpack=False) #[0] = Länge L_1/cm, [1] = Länge L_2/cm
data_mag_Moment = np.loadtxt('data/data_magnetisches_Moment.txt', unpack=False) # [0] = Stromstärke I/A, [1] = Schwingungsdauer T/s
data_Erdmagnetfeld = np.loadtxt('data/data_Erdmagnetfeld.txt', unpack=False) # [0] = Schwingungsdauer T/s

# Messwerte in SI Einheiten umrechnen

data_Schubmodul[1] = data_Schubmodul[1]/1000 # D/m
data_L[0] = data_L[0]/100 # L_1/m
data_L[1] = data_L[1]/100 # L_2/m

# weitere benötigte Größen

m_K = ufloat(512.2, 0.0004*512.2)/1000 # Masse der Kugel in kg
D_K = ufloat(50.76, 0.00007*50.76)/1000 # Kugeldurchmesser in m
theta_Kh = 0.25*1e-07 # Trägheitsmoment der Kugelhalterung in kgm^2

n_HS = 390 # Windungszahl Helmholtzspule
R_HS = 78/1000 # Radius Helmholtzspule in m
mu_0 = 4 * np.pi *1e-07 # in N/A^2

##### Auswertung 4.1

L_ges = data_L[0] + data_L[1] # Array Gesamtlängen
L = ufloat(np.mean(L_ges), np.std(L_ges)) # Gesamtlänge L in m

T = ufloat(np.mean(data_Schubmodul[0]), np.std(data_Schubmodul[0])) # Schwingungsdauer T in s

R = ufloat(np.mean(data_Schubmodul[1]), np.std(data_Schubmodul[1]))/2 # Drahtradius R in m

theta_K = (2 * m_K *(D_K/2)**2)/5 # Trägheitsmoment Kugelhalterung

G = (8 * np.pi * (theta_K + theta_Kh) * L)/(T**2 * R**4) # Schubmodul in kg/s^2

# Ergebnisse abspeichern

text_file.write('Auswertung 4.1' + '\n')
text_file.write('Länge L = ' + str(L) + '\n')
text_file.write('Drahtradius R = ' + str(R) + '\n')
text_file.write('Trägheitsmoment Kugel theta_K = ' + str(theta_K) + '\n')
text_file.write('Schwingungsdauer T = ' + str(T) + '\n')
text_file.write('Schubmodul G = ' + str(G) + '\n' + '\n')

##### Auswertung 4.2

# Daten für Regression

x = 1 / (data_mag_Moment[1]**2) # 1/T^2 in 1/s^2
y = (4/5)**(3/2) * mu_0 * n_HS * data_mag_Moment[0] / R_HS # Magnetfelder der Helmholtzspule in T

def f(x, a, b):
	return a * x + b

params, covariance = curve_fit(f, x, y)

errors = np.sqrt(np.diag(covariance))

a = ufloat(params[0], errors[0])
b = ufloat(params[1], errors[1])

x_plot = np.linspace(0, 0.05)

plt.plot(x, y, 'rx', label="Messergebnisse")
plt.plot(x_plot, f(x_plot, *params), 'b-', label='Regressionsgerade')
plt.legend(loc='best')
plt.xlabel(r'$\frac{1}{T^2}/ \frac{1}{s^2}$')
plt.ylabel('B/T')
plt.savefig('build/Plot.pdf')

m = (4 * np.pi**2 * (theta_K + theta_Kh))/a # magnetisches Moment in kgm^2/Ts^2

text_file.write('Auswertung 4.2' + '\n')
text_file.write('Daten x = ' + str(x) + '\n')
text_file.write('Daten y = ' + str(y) + '\n')
text_file.write('Steigung a = ' + str(a) + '\n')
text_file.write('y-Achsenabschnitt b = ' + str(b) + '\n')
text_file.write('magnetisches Moment m = ' + str(m) + '\n' + '\n')



##### Auswertung 4.3

T_Erde = ufloat(np.mean(data_Erdmagnetfeld[0]), np.std(data_Erdmagnetfeld[0]))

B_Erde = (4 * np.pi**2 * (theta_K + theta_Kh))/(m * T_Erde**2) - (np.pi * G * R**4)/(2 * L * m)

text_file.write('Auswertung 4.3' + '\n')
text_file.write('Schwingungsdauer T in s = ' + str(T_Erde) + '\n')
text_file.write('erdmagnetfeld B in T = ' + str(B_Erde) + '\n')
