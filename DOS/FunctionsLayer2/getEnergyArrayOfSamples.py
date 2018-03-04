# -*- coding: utf-8 -*-

import numpy as np


from DOS.FunctionsLayer1.getNumberMatrix import generateNumberMatrix
from DOS.FunctionsLayer1.convertNumberMatrix2SpinConfigs import \
                convertNumberMatrix2SpinConfigs
from DOS.FunctionsLayer1.getEnergyOfSpinConfig import getEnergyOfConfig
                


def getSampleEnergyArray(**args):
    samples_matrix = generateNumberMatrix(**args)
    sample_spinConfigsMatrix = convertNumberMatrix2SpinConfigs(samples_matrix, 
                                                         **args)
    
    sampleEnergy_list=[]
    for s in range(sample_spinConfigsMatrix.shape[0]):
        sampleSpinConfig = sample_spinConfigsMatrix[s, :]
        sampleEnergy_list.append(getEnergyOfConfig(sampleSpinConfig, **args))
    return np.array(sampleEnergy_list)


        
    
#### test
#from DOS.FunctionsLayer1.Lattices.latticeConstructor import constructLattice
#np.random.seed(1201)
#N1=4
#N2=4
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
#args['N_samples']=10
#sampleEnergy_array = getSampleEnergyArray(**args)

