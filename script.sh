#!/bin/bash

Python loraDirMulBSFixe.py 1600 1002000 1 5011200000 6

"""
for j in 1600 1700 1800 
do
    	Python loraDirMulBSK-mean.py $j 1002000 1 5011200000 6
	Python loraDirMulBSK-medoids.py $j 1002000 1 5011200000 6
	Python loraDirMulBSMean-shifts.py $j 1002000 1 5011200000 
	Python loraDirMulBSFixe.py $j 1002000 1 5011200000 6
done
"""
