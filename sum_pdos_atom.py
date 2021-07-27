#!/usr/bin/env python
# coding: utf-8

# In[36]:


'''
I have s,p (also d, but not at the moment) PDOS calculated for several
atoms. I want to have a sum for all atoms. Separately s and p.

for s we have

Energy, LDOS, PDOS columns

for p we have

Energy, LDOS, Pz-PDOS, Px-PDOS, Py-PDOS


TASK: 
-----
find sum for all atoms (= Energy, Sum of LDOS, Sum of Pz-PDOS, 
            Sum of Px-PDOS, Sum of Py-PDOS).



**NOTE: in a single directory keep on one type of states of atoms (may be same or different 
        atoms); e.g. s, p, or d only for B atoms !!***

author: skumar
date: 18, Feb, 2021

tested by Andrey Lyalin on Feb, 2021
'''
import numpy as np
import glob


file = glob.glob('chi3.pdos_atm*')

print('file[0]: {}'.format(file[0]))

dataa = np.loadtxt(file[0], skiprows = 1)
# print(data[0])
print(np.shape(data))
energy = dataa[:, 0]
print(energy[0:10])


data_summed = np.zeros_like(dataa)
print('shape of data_summed: {}'.format(np.shape(data_summed)))
dos_tot = []
dos_s = []
dos_px = []
dos_py = []
dos_pz = []

for ifile in file:
    print('file name: {}'.format(ifile))

    
    dos_tot_dummy = []
    dos_s_dummy = []
    dos_px_dummy = []
    dos_py_dummy = []
    dos_pz_dummy = []
    #with open(ifile, 'r') as f:
    #    lines = f.readlines()
    data = np.loadtxt(ifile, skiprows = 1)
    print(np.shape(data))
    print(data[:5,:])
    if int(np.shape(data)[1]) == 5:
        print('seems unpolarised pdos of p states of atoms present!!')
        colums = 5
        for i in range(colums):
            if i == 0:
                data_summed[:,i] = energy
            if i > 0:
                data_summed[:,i] += data[:,i]
        
        
    elif int(np.shape(data)[1]) == 3:
        print('seems unpolarised pdos of s states of atoms present!!')
        colums = 3
        for i in range(colums):
            if i == 0:
                data_summed[:,i] = energy
            if i > 0:
                data_summed[:,i] += data[:,i]
        
        
    elif int(np.shape(data))[1] == 7:
        print('seems unpolarised pdos of d states of atoms present!!')
        colums = 7
        for i in range(colums):
            if i == 0:
                data_summed[:,i] = energy
            if i > 0:
                data_summed[:,i] += data[:,i]
        
    else:
        print('something wrong wfc pdos files.. exiting')
        raise Exception('exting !!')
    
    
    #data_summed[1] += data[1]
# print(np.shape(data_summed))
# print(data_summed[:5,:])
filename = 'pdos_summed.dat'
print('writing data in file {} '.format(filename))
# with open(filename) as f:
#     lines = f.readlines(filename)
#     for i in range(len(lines)):
#         f.write('')
np.savetxt(filename, data_summed) #, comments='# energy pdos_total 1 2 3 ')


# In[ ]:




