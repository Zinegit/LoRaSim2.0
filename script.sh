#!/bin/bash

"""
for j in 600 700
do
	
	for i in $(seq 10)	
	do
    		Python loraDirMulBSK-means.py $j 1002000 1 5011200000 6
		Python loraDirMulBSK-medoids.py $j 1002000 1 5011200000 6
		Python loraDirMulBSMean-shifts.py $j 1002000 1 5011200000 
		Python loraDirMulBSFixe.py $j 1002000 1 5011200000 6
	done
done
"""

for j in 50 100 150 200 250 300 350 400
do
	python GenerateNodesPlaced.py $j
	for i in $(seq 10)	
	do		
		python loraDirMulBSClusterK-means.py 1002000 1 5011200000 6
	done
done
