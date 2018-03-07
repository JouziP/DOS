# -*- coding: utf-8 -*-


import numpy as np


from DOS.BasicFunctions.generateNumberArray import generateNumberArray
#######
#from FunctionsLayer1.getNumberMatrix import generateNumberMatrix
from DOS.FunctionsLayer1.convertNumberMatrix2SpinConfigs import \
                convertNumberMatrix2SpinConfigs
from DOS.FunctionsLayer1.getEnergyOfSpinConfig import getEnergyOfConfig
###################                

def is_sampleArray_new_in_sample_arrays(samples_array_list, samples_array):
    for sampledNumberArray in samples_array_list:
        diff = [ sampledNumberArray[0, i] - samples_array[0, i]\
                for i in range(samples_array.shape[1]) ]
#        print diff
        if diff==[0 for i in range(samples_array.shape[1])]:
            return 0
        else:
            pass
    return 1
####################

def updateNumberArray(samples_array, max_n_spins_in_basket):
    num_Numbers= samples_array.shape[1]
    samples_array_new = np.copy(samples_array)
    ##
    col = np.random.randint(num_Numbers)
    N_new = np.random.randint(2**max_n_spins_in_basket)
    samples_array_new[0, col] = N_new
    return samples_array_new
    
    


def getSampleEnergyArray_MC(beta, scratch=True, **args):
    N_spins = args['N_spins']
    max_n_spins_in_basket = args['max_n_spins_in_basket']
    N_warm_up = args['N_warm_up']
    #######
    sampledConfigs_list=[]
    sampledEnergy_list=[]
    samples_array_list=[]
    ##########################################################################
    if scratch==True:
        samples_array = generateNumberArray(N_spins, max_n_spins_in_basket)
        samples_array = np.matrix(samples_array)
        sample_spinConfigsArray = convertNumberMatrix2SpinConfigs(samples_array, 
                                                                  **args)
        energy = getEnergyOfConfig(sample_spinConfigsArray[0, :], **args)
    else:
        sample_spinConfigsArray = args['sample_spinConfigsArray_init']
        energy = args['energy_init']
        samples_array = args['samples_array_init']
    ##########################################################################
    ##########################################################################
    for n_warmup in range(N_warm_up):
        ###  metropolis algo
#        samples_array_new = generateNumberArray(N_spins, max_n_spins_in_basket)
        samples_array_new =updateNumberArray(samples_array, max_n_spins_in_basket)
#        samples_array_new = np.matrix(samples_array_new)
        sample_spinConfigs_new = convertNumberMatrix2SpinConfigs(samples_array_new, 
                                                             **args)
        energy_new = getEnergyOfConfig(sample_spinConfigs_new[0, :], **args)
        transition_prob = np.exp(-beta* ( energy_new - energy) )
        if transition_prob>=1:
            sample_spinConfigsArray = sample_spinConfigs_new
            energy = energy_new
            samples_array = samples_array_new
        else:
            r = np.random.uniform(0,1.0)
            if r<transition_prob:
                sample_spinConfigsArray = sample_spinConfigs_new
                energy = energy_new
                samples_array = samples_array_new
    #######                
    N_samples = args['N_samples']
    #
    sampledConfigs_list.append(sample_spinConfigsArray[0, :])
    sampledEnergy_list.append(energy)
    samples_array_list.append(samples_array)
#    print '----------------'
#    print samples_array_list
    #
    for n_sample in range(N_samples-1):
        ###  metropolis algo
#        print n_sample
        samples_array_new =updateNumberArray(samples_array, max_n_spins_in_basket)
#        samples_array_new = generateNumberArray(N_spins, 
#                                                max_n_spins_in_basket)
#        samples_array_new = np.matrix(samples_array_new)
        sample_spinConfigs_new = convertNumberMatrix2SpinConfigs(samples_array_new, 
                                                             **args)
        energy_new = getEnergyOfConfig(sample_spinConfigs_new[0, :], 
                                                             **args)
        ############
        if is_sampleArray_new_in_sample_arrays(samples_array_list, 
                                               samples_array_new)!=0:
            sampledConfigs_list.append(sample_spinConfigs_new[0, :])
            sampledEnergy_list.append(energy_new)
            samples_array_list.append(samples_array_new)
        ############
        transition_prob = np.exp(-beta* ( energy_new - energy) )
        if transition_prob>=1:
            sample_spinConfigsArray = sample_spinConfigs_new
            energy = energy_new
            samples_array = samples_array_new
        else:
            r = np.random.uniform(0,1.0)
            if r<transition_prob:
                sample_spinConfigsArray = sample_spinConfigs_new
                energy = energy_new
                samples_array = samples_array_new
        #######       
#        print '----------------'
#        print samples_array_list
        
        #
    #############  for the next step:
    args['sample_spinConfigsArray_init'] = sample_spinConfigsArray
    args['energy_init'] = energy
    args['samples_array_init']  = samples_array
    #############
    
    return np.array(sampledEnergy_list), args #, np.matrix(sampledConfigs_list)



#### test 
#from DOS.FunctionsLayer1.Lattices.latticeConstructor import constructLattice
#np.random.seed(1201)
#N1=10
#N2=10
##
#args={}
#args['J_const']=1.0
#args['E_field']=0.0
#args['power']=3.0
#args['a1_x']=1.0
#args['a1_y']=0.0
###
#args['a2_x']=0.0
#args['a2_y']=1.0
##
#args['N1'] = N1
#args['N2'] = N2
#args['N_spins']=N1*N2
#args['first_neighb']=True
#neighbors_tables_list = constructLattice(**args)
#args['neighbors_table']=neighbors_tables_list
##
#args['max_n_spins_in_basket']=50
#args['N_samples']=10
#####
#beta = 20.0
#args['num_MC'] = 1
#rslt = getSampleEnergyArray_MC(beta , **args)
#print rslt
