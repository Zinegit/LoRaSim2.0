#!/bin/bash

for i in $(seq 32)
do
	Python loraDirMulBSK-mean.py 400 1002000 1 5011200000 6
	Python loraDirMulBSK-medoids.py 400 1002000 1 5011200000 6
	Python loraDirMulBSMean-shifts.py 400 1002000 1 5011200000 
	Python loraDirMulBSFixe.py 400 1002000 1 5011200000 6
done

for j in 500 600 700 800 900 1000
do
	for i in $(seq 50)
	do
    		Python loraDirMulBSK-mean.py $j 1002000 1 5011200000 6
		Python loraDirMulBSK-medoids.py $j 1002000 1 5011200000 6
		Python loraDirMulBSMean-shifts.py $j 1002000 1 5011200000 
		Python loraDirMulBSFixe.py $j 1002000 1 5011200000 6
	done
done

