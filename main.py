#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: evandro
"""
import timeit
import numpy as np
from scipy.spatial.transform import Rotation as R

from euler_from_quat import euler_from_quat

r = R.random(1000)
t = list(range(r.as_quat().shape[0]))

#%%
seqs_proper = ['zyz','zxz','xyx','xzx','yxy','yzy']
seqs_tait = ['zyx','zxy','xyz','xzy','yxz','yzx']
seqs = seqs_proper + seqs_tait

#%% benchmark

time_quat = []
time_mat = []
time_ratio = []
err = []

# time benchmark
tests = 50
for s in seqs:
    time_quat.append(timeit.timeit('r.as_euler(s, algorithm = \'from_quat\')', number = tests, globals=globals()))
    time_mat.append(timeit.timeit('euler_from_quat(r, s)', number = tests, globals=globals()))
    time_ratio.append(time_mat[-1] / time_quat[-1])

# result comparison
for s in seqs:    
    euler_scipy = r.as_euler(s, algorithm = 'from_matrix')
    euler_test = r.as_euler(s, algorithm = 'from_quat')

    euler_err = euler_scipy - euler_test
    euler_err = (euler_err + np.pi) % (2 * np.pi) - np.pi
    err.append(sum(sum(abs(euler_err))))
    
#%%
print(f'seq & Our algorithm (s) & Shuster algorithm (s) & Ratio \\\\ \\hline')
for i in range(len(seqs)):
    print(f'{seqs[i].upper()} & ${time_quat[i]:.3f}$ s & ${time_mat[i]:.3f}$ s & ${time_mat[i] / time_quat[i]:.3f}$ \\\\ \\hline')
print(f'{tests} tests')
