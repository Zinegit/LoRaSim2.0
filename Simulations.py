import numpy as np
import matplotlib.pyplot as plt
from math import *

dataFixe = np.loadtxt("exp1BSFixe6.dat")
datakmeans = np.loadtxt("exp1BSK-means6.dat")
datakmedoids = np.loadtxt("exp1BSK-medoids6.dat")
datamean_shifts = np.loadtxt("exp1BSMean-shifts6.dat")

datakmeanscluster = np.loadtxt("exp1BSClusterK-mean6.dat")
datakmedoidscluster = np.loadtxt("exp1BSClusterK-medoids6.dat")

datamoves = np.loadtxt("moves.dat")

nrNodes = np.array([50, 100, 150, 200, 250, 300, 350, 400, 500, 600, 700])
nrNodes_cluster = np.array([50, 100, 150, 200, 250, 300])

DERSFixe = dataFixe[:, 1]
DERSFixe_lol = dataFixe[:, 0]
DERSkmeans = datakmeans[:, 1]
DERSkmeans_lol = datakmeans[:, 0]
DERSkmedoids = datakmedoids[:, 1]
DERSkmedoids_lol = datakmedoids[:, 0]
DERSmean_shifts = datamean_shifts[:, 1]
DERSmean_shifts_lol = datamean_shifts[:, 0]

DERSkmeanscluster = datakmeanscluster[:, 1]
DERSkmeanscluster_lol = datakmeanscluster[:, 0]
DERSkmedoidscluster = datakmedoidscluster[:, 1]
DERSkmedoidscluster_lol = datakmedoidscluster[:, 0]

DERSmoves = datamoves[:]
iterations = np.zeros(139)
it = [10 * i for i in range(139)]
for i in range(len(it)):
    iterations[i] = it[i]
    
print iterations
print DERSmoves

DERFixe = np.zeros(11)
DERkmeans = np.zeros(11)
DERkmedoids = np.zeros(11)
DERmean_shifts = np.zeros(11)

DERkmeanscluster = np.zeros(6)
DERkmedoidscluster = np.zeros(6)

DERFixe_V = np.zeros(8)
DERkmeans_V = np.zeros(8)
DERkmedoids_V = np.zeros(8)
DERmean_shifts_V = np.zeros(8)

#moyenne des valeurs experimentales
### Fixe
"""
for j in range(8):
    DERFixe_moyen = 0
    DERFixe_variance = 0
    for i in range(50):
        DERFixe_moyen += DERSFixe[i + 50*j]
    DERFixe_moyen = DERFixe_moyen/50
    for k in range(50):
        terme = pow((DERSFixe[k + 50*j] - DERFixe_moyen), 2)
        DERFixe_variance += terme
    DERFixe_V[j] = DERFixe_variance
    DERFixe[j] = DERFixe_moyen

j = 8
DERFixe_moyen = 0
for i in range(1, 23):
    DERFixe_moyen += DERSFixe[i + 50*j]
    print DERSFixe_lol[i + 50*j]
DERFixe_moyen = DERFixe_moyen/22
DERFixe[j] = DERFixe_moyen

j = 9
DERFixe_moyen = 0
for i in range(1, 11):
    DERFixe_moyen += DERSFixe[i + 50*8 + 22]
    print DERSFixe_lol[i + 50*8 + 22]
DERFixe_moyen = DERFixe_moyen/10
DERFixe[j] = DERFixe_moyen

j = 10
DERFixe_moyen = 0
for i in range(1, 11):
    DERFixe_moyen += DERSFixe[i + 50*8 + 22 + 10]
    print DERSFixe_lol[i + 50*8 + 22 + 10]
DERFixe_moyen = DERFixe_moyen/10
DERFixe[j] = DERFixe_moyen
"""
"""
for l in range(1, 13):
    print DERSFixe_lol[50 * (j+1) + l]
    DERFixe[j + l] = DERSFixe[50*(j+1) + l]
"""
### K-means
"""
for j in range(8):
    DERkmeans_moyen = 0
    DERkmeans_variance = 0
    for i in range(50):
        DERkmeans_moyen += DERSkmeans[i + 50*j]
    DERkmeans_moyen = DERkmeans_moyen/50
    for k in range(50):
        terme = pow((DERSkmeans[k + 50*j] - DERkmeans_moyen), 2)
        DERkmeans_variance += terme
    DERkmeans_V[j] = DERkmeans_variance
    DERkmeans[j] = DERkmeans_moyen
    #print DERkmeans

j = 8
DERkmeans_moyen = 0
for i in range(1, 22):
    DERkmeans_moyen += DERSkmeans[i + 50*j]
    print DERSkmeans_lol[i + 50*j]
DERkmeans_moyen = DERkmeans_moyen/21
DERkmeans[j] = DERkmeans_moyen

j = 9
DERkmeans_moyen = 0
for i in range(1, 11):
    DERkmeans_moyen += DERSkmeans[i + 50*8 + 21]
    print DERSkmeans_lol[i + 50*8 + 21]
DERkmeans_moyen = DERkmeans_moyen/10
DERkmeans[j] = DERkmeans_moyen

j = 10
DERkmeans_moyen = 0
for i in range(1, 11):
    DERkmeans_moyen += DERSkmeans[i + 50*8 + 21 + 10]
    print DERSkmeans_lol[i + 50*8 + 21 + 10]
DERkmeans_moyen = DERkmeans_moyen/10
DERkmeans[j] = DERkmeans_moyen
"""
"""
for l in range(1, 13):
    DERkmeans[j + l] = DERSkmeans[50*(j+1) + l]
"""
### K-medoids
"""
for j in range(8):
    DERkmedoids_moyen = 0
    DERkmedoids_variance = 0
    for i in range(50):
        DERkmedoids_moyen += DERSkmedoids[i + 50*j]
    DERkmedoids_moyen = DERkmedoids_moyen/50
    for k in range(50):
        terme = pow((DERSkmedoids[k + 50*j] - DERkmedoids_moyen), 2)
        DERkmedoids_variance += terme
    DERkmedoids_V[j] = DERkmedoids_variance
    DERkmedoids[j] = DERkmedoids_moyen


j = 8
DERkmedoids_moyen = 0
for i in range(1, 23):
    DERkmedoids_moyen += DERSkmedoids[i + 50*j]
    print DERSkmedoids_lol[i + 50*j]
DERkmedoids_moyen = DERkmedoids_moyen/22
DERkmedoids[j] = DERkmedoids_moyen

j = 9
DERkmedoids_moyen = 0
for i in range(1, 11):
    DERkmedoids_moyen += DERSkmedoids[i + 50*8 + 22]
    print DERSkmedoids_lol[i + 50*8 + 22]
DERkmedoids_moyen = DERkmedoids_moyen/10
DERkmedoids[j] = DERkmedoids_moyen

j = 10
DERkmedoids_moyen = 0
for i in range(1, 11):
    DERkmedoids_moyen += DERSkmedoids[i + 50*8 + 22 + 10]
    print DERSkmedoids_lol[i + 50*8 + 22 + 10]
DERkmedoids_moyen = DERkmedoids_moyen/10
DERkmedoids[j] = DERkmedoids_moyen
"""
"""
for l in range(1, 13):
    DERkmedoids[j + l] = DERSkmedoids[50*(j+1) + l]
"""
  
### Mean shift
"""
for j in range(8):
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
"""
j = 0
DERmean_shifts_moyen = 0
for i in range(0, 13):
    DERmean_shifts_moyen += DERSmean_shifts[i]
    print DERSmean_shifts_lol[i]
DERmean_shifts_moyen = DERmean_shifts_moyen/13
DERmean_shifts[j] = DERmean_shifts_moyen

j = 1
DERmean_shifts_moyen = 0
for i in range(0, 16):
    DERmean_shifts_moyen += DERSmean_shifts[13 + i]
    print DERSmean_shifts_lol[13 + i]
DERmean_shifts_moyen = DERmean_shifts_moyen/16
DERmean_shifts[j] = DERmean_shifts_moyen

j = 2
DERmean_shifts_moyen = 0
for i in range(0, 16):
    DERmean_shifts_moyen += DERSmean_shifts[13 + 16 + i]
    print DERSmean_shifts_lol[13 + 16 + i]
DERmean_shifts_moyen = DERmean_shifts_moyen/16
DERmean_shifts[j] = DERmean_shifts_moyen

j = 3
DERmean_shifts_moyen = 0
for i in range(0, 8):
    DERmean_shifts_moyen += DERSmean_shifts[13 + 16 + 16 + i]
    print DERSmean_shifts_lol[13 + 16 + 16 + i]
DERmean_shifts_moyen = DERmean_shifts_moyen/8
DERmean_shifts[j] = DERmean_shifts_moyen

j = 4
DERmean_shifts_moyen = 0
for i in range(0, 11):
    DERmean_shifts_moyen += DERSmean_shifts[13 + 16 + 16 + 8 + i]
    print DERSmean_shifts_lol[13 + 16 + 16 + 8 + i]
DERmean_shifts_moyen = DERmean_shifts_moyen/11
DERmean_shifts[j] = DERmean_shifts_moyen

j = 5
DERmean_shifts_moyen = 0
for i in range(0, 5):
    DERmean_shifts_moyen += DERSmean_shifts[13 + 16 + 16 + 8 + 11 + i]
    print DERSmean_shifts_lol[13 + 16 + 16 + 8 + 11 + i]
DERmean_shifts_moyen = DERmean_shifts_moyen/5
DERmean_shifts[j] = DERmean_shifts_moyen

j = 6
DERmean_shifts_moyen = 0
for i in range(0, 11):
    DERmean_shifts_moyen += DERSmean_shifts[13 + 16 + 16 + 8 + 11 + 5 + i]
    print DERSmean_shifts_lol[13 + 16 + 16 + 8 + 11 + 5 + i]
DERmean_shifts_moyen = DERmean_shifts_moyen/11
DERmean_shifts[j] = DERmean_shifts_moyen

j = 7
DERmean_shifts_moyen = 0
for i in range(0, 4):
    DERmean_shifts_moyen += DERSmean_shifts[13 + 16 + 16 + 8 + 11 + 5 + 11 + i]
    print DERSmean_shifts_lol[13 + 16 + 16 + 8 + 11 + 5 + 11 + i]
DERmean_shifts_moyen = DERmean_shifts_moyen/4
DERmean_shifts[j] = DERmean_shifts_moyen

j = 8
DERmean_shifts_moyen = 0
for i in range(0, 3):
    DERmean_shifts_moyen += DERSmean_shifts[13 + 16 + 16 + 8 + 11 + 5 + 11 + 4 + i]
    print DERSmean_shifts_lol[13 + 16 + 16 + 8 + 11 + 5 + 11 + 4 +i]
DERmean_shifts_moyen = DERmean_shifts_moyen/3
DERmean_shifts[j] = DERmean_shifts_moyen

j = 9
DERmean_shifts_moyen = 0
for i in range(0, 2):
    DERmean_shifts_moyen += DERSmean_shifts[13 + 16 + 16 + 8 + 11 + 5 + 11 + 4 + 3 + i]
    print DERSmean_shifts_lol[13 + 16 + 16 + 8 + 11 + 5 + 11 + 4 + 3 + i]
DERmean_shifts_moyen = DERmean_shifts_moyen/2
DERmean_shifts[j] = DERmean_shifts_moyen

j = 10
DERmean_shifts_moyen = 0
for i in range(0, 1):
    DERmean_shifts_moyen += DERSmean_shifts[13 + 16 + 16 + 8 + 11 + 5 + 11 + 4 + 3 + 2 + i]
    print DERSmean_shifts_lol[13 + 16 + 16 + 8 + 11 + 5 + 11 + 4 + 3 + 2 + i]
DERmean_shifts_moyen = DERmean_shifts_moyen/1
DERmean_shifts[j] = DERmean_shifts_moyen
"""
"""
### K-means clustering
for j in range(6):
    DERkmeans_moyen_cluster = 0
    DERkmeans_variance_cluster = 0
    for i in range(10):
        DERkmeans_moyen_cluster += DERSkmeanscluster[i + 10*j]
    DERkmeans_moyen_cluster = DERkmeans_moyen_cluster/10
    DERkmeanscluster[j] = DERkmeans_moyen_cluster

### K-medoids clustering
for j in range(6):
    DERkmedoids_moyen_cluster = 0
    DERkmedoids_variance_cluster = 0
    for i in range(10):
        DERkmedoids_moyen_cluster += DERSkmedoidscluster[i + 10*j]
    DERkmedoids_moyen_cluster = DERkmedoids_moyen_cluster/10
    DERkmedoidscluster[j] = DERkmedoids_moyen_cluster
"""
### Trace des moyennes
"""
plt.figure    

plt.axis([50, 700, 0.65, 1])
plt.grid()

plt.title("Evolution du DER en fonction du nombre de nodes du reseau pour chaque algorithme")
plt.xlabel("nombre de nodes")
plt.ylabel("DER")

print len(nrNodes), len(DERkmeans)
plt.plot(nrNodes, DERkmeans, label = "K-mean")
plt.plot(nrNodes, DERkmedoids, label = "K-medoids")
plt.plot(nrNodes, DERFixe, label = "Fixe")
plt.plot(nrNodes, DERmean_shifts, "--", label = "Mean Shifts")
"""

### Trace des variances
"""
plt.figure    

plt.axis([50, 500, 0.7, 0.09])
plt.grid()

plt.title("Evolution de la variance du DER en fonction du nombre de nodes du reseau pour chaque algorithme")
plt.xlabel("nombre de nodes")
plt.ylabel("Variance du DER")

plt.plot(nrNodes, DERkmeans_V, label = "K-mean")
plt.plot(nrNodes, DERkmedoids_V, label = "K-medoids")
plt.plot(nrNodes, DERFixe_V, label = "Fixe")
#plt.plot(nrNodes, DERmean_shifts_V, label = "Mean Shifts")
"""

### Trace des moyennes clusterees
"""
plt.figure    

plt.axis([50, 400, 0.65, 1])
plt.grid()

plt.title("Evolution du DER en fonction du nombre de nodes du reseau pour chaque algorithme")
plt.xlabel("nombre de nodes")
plt.ylabel("DER")

print len(nrNodes_cluster), len(DERkmeans)
plt.plot(nrNodes_cluster, DERkmeanscluster, label = "K-means")
plt.plot(nrNodes_cluster, DERkmedoidscluster, label = "K-medoids")
"""
###Moves

plt.figure    

plt.axis([50, 1400, 0.7, 1])
plt.grid()

plt.title("Evolution du DER au cours du temps")
plt.xlabel("distance parcourue(m)")
plt.ylabel("DER")

print len(iterations), len(DERSmoves)
plt.plot(iterations, DERSmoves)

plt.legend(loc='bottom left')

plt.show()    

    
