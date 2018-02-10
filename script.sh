#!/bin/bash

"""
for i in $(seq 32)
do
	Python loraDirMulBSK-mean.py 400 1002000 1 5011200000 6
	Python loraDirMulBSK-medoids.py 400 1002000 1 5011200000 6
	Python loraDirMulBSMean-shifts.py 400 1002000 1 5011200000 
	Python loraDirMulBSFixe.py 400 1002000 1 5011200000 6
done
"""

for j in 1300 1400 1500 1600 1700
do
    	Python loraDirMulBSK-mean.py $j 1002000 1 5011200000 6
	Python loraDirMulBSK-medoids.py $j 1002000 1 5011200000 6
	Python loraDirMulBSMean-shifts.py $j 1002000 1 5011200000 
	Python loraDirMulBSFixe.py $j 1002000 1 5011200000 6
done

