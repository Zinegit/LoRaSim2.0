import math
import os

GL = 0
Ptx = 14
d0 = float(40)
Lpld0 = 127.41
gamma = 2.08
distance = float(1)

print distance
print d0
print (distance/d0)
Prx = Ptx + GL - Lpld0 + 10*gamma*math.log10(distance/d0)

fname = "validation.dat"
    
for i in range(1, 600):
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

