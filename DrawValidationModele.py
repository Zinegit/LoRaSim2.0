import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("validation.dat")
distances = np.asarray(data[:, 0])
Prxs = np.asarray(data[:, 1])

plt.figure    

plt.grid()

plt.title("puissance recue en fonction de la distance avec l'emetteur")
plt.xlabel("distance (m)")
plt.ylabel("rssi (dBm)")

plt.plot(distances, Prxs)
plt.show()    
    
    
