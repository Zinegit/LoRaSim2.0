import numpy as np
import matplotlib.pyplot as plt

dataFixe = np.loadtxt("exp1BSFixe6.dat")
dataKmean = np.loadtxt("exp1BSK-mean6.dat")
nrNodes = np.array([0, 50, 100, 150])
DERS = dataKmean[:, 1]
DER = np.zeros(4)

for j in range(4):
    DER_moyen = 0
    for i in range(50):
        DER_moyen += DERS[i + 50*j]
    DER_moyen = DER_moyen/50
    DER[j] = DER_moyen
print DER
print nrNodes
#dataKmedoids = loadtxt("exp1BSK-medoids6.dat")
#dataKmeanShifts = loadtxt("exp1BSMean-shifts6.dat")
    
plt.figure    

plt.axis([0, 1000, 0, 1])
plt.grid()

plt.title("Evolution du DER en fonction du nombre de nodes du reseau pour chaque algorithme")
plt.xlabel("nombre de nodes")
plt.ylabel("DER")

plt.plot(nrNodes, DER)
plt.show()    
    
    
