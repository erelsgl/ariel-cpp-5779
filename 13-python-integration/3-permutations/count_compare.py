#!python3

import time

import count_permutations

import cppyy
cppyy.include("count_permutations.cpp")

use_cpp = False

if use_cpp:
	print("Using C++ implementation")
else:
	print("Using Python implementation")

for N in range(5,12):
	print ("Permutations of 1..{}:".format(N), flush=True)
	start = time.clock()
	if use_cpp:
		count = cppy	y.gbl.count_permutations(N)
	else:
		count = count_permutations.count_permutations(N) 
	end = time.clock()
	duration_in_seconds = end-start
	print("  {} permutations calculated in {} seconds".format(count, duration_in_seconds), flush=True)