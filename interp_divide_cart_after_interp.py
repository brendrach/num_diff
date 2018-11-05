"""
@author: Brendan Drachler
@purpose:   Divides prim quantites in the interpolated cartesian init file. These new
            quantities will then be used for initial data in a 2D cartesian run.
"""

#importing libraries
import h5py
import numpy as np
import math

#loading in the necessary files - rdump_start_other.h5 is the output file 
#after interpolation
cart_data = 'rdump_start_other.h5'


#grants read/write ability for files
cart_file = h5py.File(cart_data, 'r+')

#telling Python where to access the necessary quantities
rho = cart_file['rho_dest']
uu = cart_file['uu_dest']
v1 = cart_file['v1_dest']
v2 = cart_file['v2_dest']
v3 = cart_file['v3_dest']
gdet_cart = cart_file['gdet']

num_x_cells = 1392
num_y_cells = 1392

#for loop that alters each quantity on the grid by recalculating it 
#and then rewriting it to the init cartesian file file.
for i in range(0, num_x_cells):
    for j in range(0, num_y_cells):
        rho_temp = rho[i,j,0]/gdet_cart[i,j,0]
        rho[i,j,0] = rho_temp
        uu_temp = uu[i,j,0]/gdet_cart[i,j,0]
        uu[i,j,0] = uu_temp
        v1_temp = v1[i,j,0]/gdet_cart[i,j,0]
        v1[i,j,0] = v1_temp
        v2_temp = v2[i,j,0]/gdet_cart[i,j,0]
        v2[i,j,0] = v2_temp
        v3_temp = v3[i,j,0]/gdet_cart[i,j,0]
        v3[i,j,0] = v3_temp

        