import numpy as np
import matplotlib.pyplot as plt

dataFixe = np.loadtxt("exp1BSFixe6.dat")
dataKmean = np.loadtxt("exp1BSK-mean6.dat")
dataKmedoids = np.loadtxt("exp1BSK-medoids6.dat")
datamean_shifts = np.loadtxt("exp1BSMean-shifts6.dat")

nrNodes = np.array([50, 100, 150, 200, 250])

DERSFixe = dataFixe[:, 1]
DERSKmean = dataKmean[:, 1]
DERSKmedoids = dataKmedoids[:, 1]
DERSmean_shifts = datamean_shifts[:, 1]

DERFixe = np.zeros(5)
DERKmean = np.zeros(5)
DERKmedoids = np.zeros(5)
DERmean_shifts = np.zeros(5)

#moyenne des valeurs experimentales
for j in range(5):
    DERFixe_moyen = 0
    for i in range(50):
        DERFixe_moyen += DERSFixe[i + 50*j]
    DERFixe_moyen = DERFixe_moyen/50
    DERFixe[j] = DERFixe_moyen
    
for j in range(5):
    DERKmean_moyen = 0
    for i in range(50):
        DERKmean_moyen += DERSKmean[i + 50*j]
    DERKmean_moyen = DERKmean_moyen/50
    DERKmean[j] = DERKmean_moyen
    
for j in range(5):
    DERKmedoids_moyen = 0
    for i in range(50):
        DERKmedoids_moyen += DERSKmedoids[i + 50*j]
    DERKmedoids_moyen = DERKmedoids_moyen/50
    DERKmedoids[j] = DERKmedoids_moyen
  
"""  
for j in range(5):
    DERmean_shifts_moyen = 0
    for i in range(50):
        DERmean_shifts_moyen += DERSmean_shifts[i + 50*j]
    DERmean_shifts_moyen = DERmean_shifts_moyen/50
    DERmean_shifts[j] = DERmean_shifts_moyen
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

plt.legend(loc='bottom left')

plt.show()    
    
    
