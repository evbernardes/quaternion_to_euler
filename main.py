#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This scrips creates random quaternion orientation data of size N, then perform
the conversion using both my algorithm and Shuster's algorithm as implemented
in the Scipy library.

We note that in order to fully compare the execution time, the algorighm should
be compiled directly inside of Scipy. 

A version of Scipy with this algorithm can be found in:
https://github.com/evbernardes/scipy
    
@author: Evandro Bernardes
"""
import timeit
import numpy as np
from scipy.spatial.transform import Rotation as R
from euler_from_quat import euler_from_quat

#%%
N = 1000 # Number of points in each test
r = R.random(N)

#%% All possible sequences
seqs_proper = ['zyz','zxz','xyx','xzx','yxy','yzy']
seqs_tait = ['zyx','zxy','xyz','xzy','yxz','yzx']
seqs = seqs_proper + seqs_tait
seqs += [s.upper() for s in seqs] # uppercase and 

#%% benchmark

time_quat = [] # time spent running our algorithm
time_mat = [] # time spent running Shuster algorithm
time_ratio = [] # ratio between both time executions
err = []

# time benchmark
for s in seqs:
    time_mat.append(timeit.timeit('r.as_euler(s)', number = 1, globals=globals()))   
    
    #%% Choose one and comment the other:
    # Compiled, if special Scipy version is used
#    time_quat.append(timeit.timeit('r.as_euler(s, algorithm = \'from_quat\')', number = 1, globals=globals()))
    
    # Non compiled, slower
    time_quat.append(timeit.timeit('euler_from_quat(r, s)', number = 1, globals=globals()))
    
    time_ratio.append(time_mat[-1] / time_quat[-1])

# result comparison
for s in seqs:    
    euler_scipy = r.as_euler(s)
    euler_test = euler_from_quat(r, s)

    euler_err = euler_scipy - euler_test
    euler_err = (euler_err + np.pi) % (2 * np.pi) - np.pi
    err.append(sum(sum(abs(euler_err))))
    
#%%
print(f'\nIf the ratio is bigger than 1, our algorithm is faster:')
print(f'seq | Our algo| Shuster | Ratio')
for i in range(len(seqs)):
    print(f'{seqs[i]} | {1000*time_quat[i]:.3f} ms | {1000*time_mat[i]:.3f} ms | {time_mat[i] / time_quat[i]:.3f}')

#printf()

print(f'\nseq | sum of differences for each test')
for i in range(len(seqs)):
    print(f'{seqs[i]} | {err[i]}')