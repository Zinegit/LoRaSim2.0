#!/bin/bash
for i in $(seq 6)
do
	for j in $(seq 100)
	do
    		Python loraDirMulBSK-mean.py 100 1002000 1 5011200000 $i
	done
done


