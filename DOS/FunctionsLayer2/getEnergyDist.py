# -*- coding: utf-8 -*-

import numpy as np
from collections import Counter


def getEnergyDist(energy_array, **args):
    _precision = 2
    energy_list = list(energy_array)
    energy_list = [np.round(energy_list[i], _precision)\
                                   for i in range(len(energy_list))]
    enegy_dict  = Counter(energy_list)
    energy_unique_list = [float(key) for key in enegy_dict.keys()]
    energy_unique_count_list = [float(val) for val in enegy_dict.values()]
    ####
    num_bins = len(energy_unique_count_list)
    print num_bins
    energy_hist=np.zeros([num_bins, 2])
    energy_hist[:, 0]=energy_unique_list
    energy_hist[:, 1]=energy_unique_count_list
    ####
    energy_hist=energy_hist[np.argsort(energy_hist[:,0])]
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


