import math
import os
import numpy as np
import matplotlib.pyplot as plt

GL = 0
Ptx = 14
d0 = float(40)
Lpld0 = 127.41
gamma = 2.08
distance = float(1)

Prx = Ptx + GL - Lpld0 + 10*gamma*math.log10(distance/d0)

data_recepteur = np.loadtxt("RecepteurTP14.txt")
data_emetteur = np.loadtxt("EmetteurTP14.txt")
data_sim = np.loadtxt("validation.dat")
data_emetteur_seuil = np.loadtxt("EmetteurTP2.txt")

latitudes_recepteur = data_recepteur[:, 0]
longitudes_recepteur = data_recepteur[:, 1]
rssi_recepteur = data_recepteur[:, 2]

latitudes_emetteur = data_emetteur[:, 0]
longitudes_emetteur = data_emetteur[:, 1]
rssi_emetteur = data_emetteur[:, 2]

distances_sim = np.asarray(data_sim[:, 0])
rssi_sim = np.asarray(data_sim[:, 1])

latitudes_emetteur_seuil = data_emetteur_seuil[:, 0]
longitudes_emetteur_seuil = data_emetteur_seuil[:, 1]
rssi_emetteur_seuil = data_emetteur_seuil[:, 2]

def convertRad(x):
    return (math.pi * x) / 180
    
def dist(lat_a_degre, lon_a_degre, lat_b_degre, lon_b_degre):
    lat_a = convertRad(lat_a_degre);
    lon_a = convertRad(lon_a_degre);
    lat_b = convertRad(lat_b_degre);
    lon_b = convertRad(lon_b_degre);
    
    R = 6378000 #Rayon de la terre en metre
    
    distance = R * (math.pi/2 - math.asin( math.sin(lat_b) * math.sin(lat_a) + math.cos(lon_b - lon_a) * math.cos(lat_b) * math.cos(lat_a)))
    return distance
    
distances_recepteur = [0 for i in range(len(latitudes_recepteur))]
for i in range(len(latitudes_recepteur)):
    distances_recepteur[i] = dist(latitudes_recepteur[0], longitudes_recepteur[0], latitudes_recepteur[i], longitudes_recepteur[i])
    
print distances_recepteur

distances_emetteur = [0 for i in range(len(latitudes_emetteur))]
for i in range(len(latitudes_emetteur)):
    distances_emetteur[i] = dist(latitudes_emetteur[0], longitudes_emetteur[0], latitudes_emetteur[i], longitudes_emetteur[i])

plt.figure    

plt.grid()

"""
plt.title("puissance recue en fonction de la distance avec l'emetteur")
plt.xlabel("distance (m)")
plt.ylabel("rssi (dBm)")

plt.plot(distances_recepteur, rssi_recepteur, label = "experience recepteur")
plt.plot(distances_emetteur, rssi_emetteur, label = "experience emetteur")
plt.plot(distances_sim, rssi_sim, label = "theorique")

plt.legend(loc='bottom left')
"""

distances_emetteur_seuil = [0 for i in range(len(latitudes_emetteur_seuil))]
for i in range(len(latitudes_emetteur_seuil)):
    distances_emetteur_seuil[i] = dist(latitudes_emetteur_seuil[0], longitudes_emetteur_seuil[0], latitudes_emetteur_seuil[i], longitudes_emetteur_seuil[i])
    
plt.title("puissance recue en fonction de la distance avec l'emetteur")
plt.xlabel("distance (m)")
plt.ylabel("rssi (dBm)")

plt.plot(distances_emetteur_seuil, rssi_emetteur_seuil)

plt.show()    
    
    
"""
     

}

fname = "validation.dat"
    
for i in range(1, 601):
    distance = float(i)
    print "distance :" + str(distance)
    print "Lpl", 10*gamma*math.log10(distance/d0)
    Prx = Ptx + GL - Lpld0 - 10*gamma*math.log10(distance/d0)
    print "Prx : ", Prx
    if os.path.isfile(fname):
        res = "\n" + str(distance) + " " + str(Prx)
    else:
        res = str(distance) + " " + str(Prx)
    with open(fname, "a") as myfile:
        myfile.write(res)
myfile.close()

"""