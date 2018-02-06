#!/bin/bash

for j in 50 100 150 200 250 300 350 400 450 500 550 600 650 700 750 800 850 900 950 1000
do
	for i in $(seq 50)
	do
    		Python loraDirMulBSK-mean.py $j 1002000 1 5011200000 6
		Python loraDirMulBSK-medoids.py $j 1002000 1 5011200000 6
		Python loraDirMulBSMean-shifts.py $j 1002000 1 5011200000 
		Python loraDirMulBSFixe.py $j 1002000 1 5011200000 6
	done
done

