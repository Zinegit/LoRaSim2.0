import math
import random
import numpy as np
import sys
import os

if len(sys.argv) >= 1:
    nrNodes = int(sys.argv[1])
#   posxBS = np.zeros(nrBS)
#   posyBS = np.zeros(nrBS)

gamma = 2.08
d0 = 40.0
Lpld0 = 127.41
maxDist = 321.98024173
maxX = 5 * maxDist * math.sin(60*(math.pi/180)) 
maxY = 5 * maxDist * math.sin(30*(math.pi/180)) 

node_positions = [[0,0] for i in range(nrNodes + 1)]

first_node = 0
fname = "nodes_placed.dat"
if os.path.isfile(fname):
    open('nodes_placed.dat', 'w').close()
    
for i in range(0, int(np.sqrt(nrNodes))):
    for j in range(0, int(np.sqrt(nrNodes))):
        posx = 120 + 10 * i 
        posy = 60 + 10 * j
        res = "\n" + str(posx) + " " + str(posy)
        with open(fname, "a") as myfile:
            myfile.write(res)
            
res = "\n" + str(700) + " " + str(800)
with open(fname, "a") as myfile:
    myfile.write(res)
    
res = "\n" + str(1400) + " " + str(100)
with open(fname, "a") as myfile:
    myfile.write(res)
    
res = "\n" + str(700) + " " + str(200)
with open(fname, "a") as myfile:
    myfile.write(res)
    
res = "\n" + str(1400) + " " + str(800)
with open(fname, "a") as myfile:
    myfile.write(res)
    
res = "\n" + str(0) + " " + str(800)
with open(fname, "a") as myfile:
    myfile.write(res)
    


