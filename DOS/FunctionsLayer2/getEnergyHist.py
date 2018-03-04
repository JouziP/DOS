# -*- coding: utf-8 -*-

import numpy as np

def getEnergyHist(energy_array, **args):
    if 'num_bins' in args:
        num_bins = args['num_bins']
    else:
        num_bins = 10
    energy_min = np.min(energy_array)
    energy_max = np.max(energy_array)
    dEnergy=(energy_max - energy_min)/num_bins
    ####
    energy_hist=np.zeros([num_bins, 2])
    for b in range(num_bins):
        energy_hist[b, 0]=energy_min + b*dEnergy
        #
        for E in energy_array:      
            #
            if E>=energy_min+b*dEnergy and E< energy_min+(b+1)*dEnergy:
                energy_hist[b, 1]+=1
    energy_hist[:, 1]=energy_hist[:, 1]
    energy_hist[:, 0]=energy_hist[:, 0]
    ####
    return energy_hist
    
    
 
#### test

#import matplotlib.pyplot as plt
#from DOS.FunctionsLayer1.Lattices.latticeConstructor import constructLattice
#from DOS.FunctionsLayer2.getSampleEnergyArray import getSampleEnergyArray
#np.random.seed(1201)
#N1=6
#N2=6
#
#args={}
#args['J_const']=1.0
#args['E_field']=0.0
#args['power']=3.0
#args['a1_x']=1.0
#args['a1_y']=0.0
##
#args['a2_x']=0.0
#args['a2_y']=1.0
#
#args['N1'] = N1
#args['N2'] = N2
#args['N_spins']=N1*N2
#args['first_neighb']=False
#neighbors_tables_list = constructLattice(**args)
#args['neighbors_table']=neighbors_tables_list
#
#args['max_n_spins_in_basket']=N1*N2/3
#args['N_samples']=5000
#sampleEnergy_array = getSampleEnergyArray(**args)
###########
#args['num_bins']=5000
###energy_array = np.array([-50, -40,-2,0,0 ,1, 2, -12, -19])
#energy_hist = getEnergyHist(sampleEnergy_array, **args)

#plt.bar(energy_hist[:,0], energy_hist[:,1])


