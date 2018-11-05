"""
@author: Brendan Drachler
@purpose:   Multiplies prim quantites in the init spherical dump file. These new
            quantities will then be used for interpolation onto a cartesian grid.
"""

#importing libraries
import h5py
import numpy as np
import math

#loading in the necessary files
sphere_data = 'rdump_start.h5'
sphere_compare_data = 'rdump_start_compare.h5'


#grants read/write ability for files
#sphere_file is a file that will be used for interpolation 
#after changing the necessary primitive quantities.
#sphere_comp_file is an exact copy of sphere_file before
#any values are altered. This is diffed later to ensure
#values are indeed being changed. It is merely a test to ensure
#the code is behaving properly. 
sphere_file = h5py.File(sphere_data, 'r+')
sphere_comp_file = h5py.File(sphere_compare_data, 'r')

#telling Python where to access the necessary quantities
rho = sphere_file['rho']
uu = sphere_file['uu']
v1 = sphere_file['v1']
v2 = sphere_file['v2']
v3 = sphere_file['v3']
gdet_sphere = sphere_file['gdet']

#telling Python where to access a copy of the unaltered quantities.
rho_comp = sphere_comp_file['rho']
uu_comp = sphere_comp_file['uu']
v1_comp = sphere_comp_file['v1']
v2_comp = sphere_comp_file['v2']
v3_comp = sphere_comp_file['v3']
gdet_sphere_comp = sphere_comp_file['gdet']

#initializing arrays for diff test - not pertinent for the purpose of the code
#this is strictly used for the verification mentioned above
diff_rho = []
diff_uu = []
diff_v1 = []
diff_v2 = []
diff_v3 = []
gdet_calc = []

#specify the number of cells in each direction so that we are iterating
#over every point on the grid.
num_r_cells = 84
num_phi_cells = 128
#for loop that alters each quantity on the grid by recalculating it 
#and then rewriting it to the to-be-interpolated file.
for i in range(0, num_r_cells):
    for j in range(0, num_phi_cells):
        rho_temp = gdet_sphere[i,0,j]*rho[i,0,j]
        rho[i,0,j] = rho_temp
        uu_temp = gdet_sphere[i,0,j]*uu[i,0,j]
        uu[i,0,j] = uu_temp
        v1_temp = gdet_sphere[i,0,j]*v1[i,0,j]
        v1[i,0,j] = v1_temp
        v2_temp = gdet_sphere[i,0,j]*v2[i,0,j]
        v2[i,0,j] = v2_temp
        v3_temp = gdet_sphere[i,0,j]*v3[i,0,j]
        v3[i,0,j] = v3_temp
        
        #appending values to the diff test arrays - just for testing.
        diff_rho.append(abs(rho[i,0,j] - rho_comp[i,0,j]))
        diff_uu.append(abs(uu[i,0,j] - uu_comp[i,0,j]))
        diff_v1.append(abs(v1[i,0,j] - v1_comp[i,0,j]))
        diff_v2.append(abs(v2[i,0,j] - v2_comp[i,0,j]))
        diff_v3.append(abs(v3[i,0,j] - v3_comp[i,0,j]))
        
        gdet_calc.append(gdet_sphere[i,0,j])
        
#if diff = [0,0,0,0,0], something is not being done right. if diff =! [0,0,0,0,0],
#the values are being rewritten 
diff = [max(diff_rho), max(diff_uu), max(diff_v1), max(diff_v2), max(diff_v3)]
print (diff)
        

    