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

node_positions = [[0,0] for i in range(nrNodes)]

first_node = 0
fname = "nodes.dat"
if os.path.isfile(fname):
    open('nodes.dat', 'w').close()
    

for i in range(0, nrNodes):    
    # this is very complex prodecure for placing nodes
    # and ensure minimum distance between each pair of nodes
    found = 0
    rounds = 0
    while (found == 0 and rounds < 100):
        posx = random.randint(0,int(maxX))
        posy = random.randint(0,int(maxY))
        #K-MEAN
        node_positions[i][0] = posx
        node_positions[i][1] = posy
        #
        if first_node == 1:
            for n in(node_positions):
                dist = np.sqrt(((abs(n[0]-posx))**2)+((abs(n[1]-posy))**2))
                if dist >= 10:
                    found = 1
                    node_positions[i][0] = posx
                    node_positions[i][1] = posy
                else:
                    rounds = rounds + 1
                    if rounds == 100:
                        print "could not place new node, giving up"
                        exit(-2)
        else:
            first_node = 1
            node_positions[0][0] = posx
            node_positions[0][1] = posy
            found = 1
    res = "\n" + str(posx) + " " + str(posy)
    with open(fname, "a") as myfile:
        myfile.write(res)
        
myfile.close()




