#! /bin/bash


for file in *.sh; do
	echo $(basename $file .sh)

done

