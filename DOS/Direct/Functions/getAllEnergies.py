#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 08:26:46 2018

@author: pejmaroni
"""


import numpy as np


from getBinaryArray import getBinaryArray

from latticeConstructor import constructLattice
from getEnergyOfSpinConfig import getEnergyOfConfig
#def getAllEnergies(N, **args):
    

N1 = 5
N2 = 5
N = N1 *N2    

args={}
args['J_const']=1.0
args['E_field']=0.0
args['power']=3.0
args['a1_x']=1.0
args['a1_y']=0.0
#
args['a2_x']=0.0
args['a2_y']=1.0

args['N1'] = N1
args['N2'] = N2
args['N_spins']=N1*N2
args['first_neighb']=False
neighbors_tables_list = constructLattice(**args)
args['neighbors_table']=neighbors_tables_list


energies=[]
for i in range(2**N):
    spin_config = getBinaryArray(N, i)
    energies.append(getEnergyOfConfig(spin_config, **args))
