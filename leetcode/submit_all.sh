#!/bin/bash

for i in `echo *\.*.py | sort -n`; do
   echo "$i"
   timeout 10s leetcode submit $i
   sleep 7 
done
