import numpy as np
import matplotlib.pyplot as plt
from math import *

dataFixe = np.loadtxt("exp1BSFixe6.dat")
dataKmean = np.loadtxt("exp1BSK-mean6.dat")
dataKmedoids = np.loadtxt("exp1BSK-medoids6.dat")
datamean_shifts = np.loadtxt("exp1BSMean-shifts6.dat")

nrNodes = np.array([50, 100, 150, 200, 250, 300, 350])

DERSFixe = dataFixe[:, 1]
DERSKmean = dataKmean[:, 1]
DERSKmedoids = dataKmedoids[:, 1]
DERSmean_shifts = datamean_shifts[:, 1]

DERFixe = np.zeros(7)
DERKmean = np.zeros(7)
DERKmedoids = np.zeros(7)
DERmean_shifts = np.zeros(7)

DERFixe_V = np.zeros(7)
DERKmean_V = np.zeros(7)
DERKmedoids_V = np.zeros(7)
DERmean_shifts_V = np.zeros(7)

#moyenne des valeurs experimentales
for j in range(7):
    DERFixe_moyen = 0
    DERFixe_variance = 0
    for i in range(50):
        DERFixe_moyen += DERSFixe[i + 50*j]
    DERFixe_moyen = DERFixe_moyen/50
    for k in range(50):
        terme = pow((DERSFixe[k + 50*j] - DERFixe_moyen), 2)
        DERFixe_variance += terme
    DERFixe_V[j] = DERFixe_variance
    print j, DERFixe_variance
    DERFixe[j] = DERFixe_moyen
    
for j in range(7):
    DERKmean_moyen = 0
    DERKmean_variance = 0
    for i in range(50):
        DERKmean_moyen += DERSKmean[i + 50*j]
    DERKmean_moyen = DERKmean_moyen/50
    for k in range(50):
        terme = pow((DERSKmean[k + 50*j] - DERKmean_moyen), 2)
        DERKmean_variance += terme
    DERKmean_V[j] = DERKmean_variance
    print j, DERKmean_variance
    DERKmean[j] = DERKmean_moyen
    
for j in range(7):
    DERKmedoids_moyen = 0
    DERKmedoids_variance = 0
    for i in range(50):
        DERKmedoids_moyen += DERSKmedoids[i + 50*j]
    DERKmedoids_moyen = DERKmedoids_moyen/50
    for k in range(50):
        terme = pow((DERSKmedoids[k + 50*j] - DERKmedoids_moyen), 2)
        DERKmedoids_variance += terme
    DERKmedoids_V[j] = DERKmedoids_variance
    print j, DERKmedoids_variance
    DERKmedoids[j] = DERKmedoids_moyen
  
"""  
for j in range(5):
    DERmean_shifts_moyen = 0
    DERmean_shifts_variance = 0
    for i in range(50):
        DERmean_shifts_moyen += DERSmean_shifts[i + 50*j]
    DERmean_shifts_moyen = DERmean_shifts_moyen/50
    for k in range(50):
        terme = pow((DERSmean_shifts[k + 50*j] - DERmean_shifts_moyen), 2)
        DERmean_shifts_variance += terme
    DERmean_shifts_V[j] = DERmean_shifts_variance
    DERmean_shifts[j] = DERmean_shifts_moyen
"""

### Trace des moyennes
"""
plt.figure    

plt.axis([50, 1000, 0, 1])
plt.grid()

plt.title("Evolution du DER en fonction du nombre de nodes du reseau pour chaque algorithme")
plt.xlabel("nombre de nodes")
plt.ylabel("DER")

plt.plot(nrNodes, DERKmean, label = "K-mean")
plt.plot(nrNodes, DERKmedoids, label = "K-medoids")
plt.plot(nrNodes, DERFixe, label = "Fixe")
#plt.plot(nrNodes, DERmean_shifts, label = "Mean Shifts")
"""
### Trace des variances
plt.figure    

plt.axis([50, 1000, 0, 0.09])
plt.grid()

plt.title("Evolution de la variance du DER en fonction du nombre de nodes du reseau pour chaque algorithme")
plt.xlabel("nombre de nodes")
plt.ylabel("Variance du DER")

plt.plot(nrNodes, DERKmean_V, label = "K-mean")
plt.plot(nrNodes, DERKmedoids_V, label = "K-medoids")
plt.plot(nrNodes, DERFixe_V, label = "Fixe")
#plt.plot(nrNodes, DERmean_shifts_V, label = "Mean Shifts")



plt.legend(loc='bottom left')

plt.show()    
    
    
