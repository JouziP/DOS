# -*- coding: utf-8 -*-

import numpy as np

from BasicFunctions.generateNumberArray import generateNumberArray


def isRepeatedSample(numberArray, samples_list):
    #
    for recordedNumberArray in samples_list:
        diff = [recordedNumberArray[i] - numberArray[i]\
                for i in range(len(numberArray))]
        if diff==[0 for i in range(len(numberArray))]:
            return 0
    return 1
        
   
def generateNumberMatrix(**args):
    N_spins = args['N_spins']
    max_n_spins_in_basket = args['max_n_spins_in_basket']
    N_samples = args['N_samples']
    sampling_method=args['sampling_method']
    ###########################
    num_baskets = (N_spins/max_n_spins_in_basket+1,
                   N_spins/max_n_spins_in_basket)\
                   [N_spins-(N_spins/max_n_spins_in_basket)*\
                    max_n_spins_in_basket==0]
    if num_baskets!=(N_spins/max_n_spins_in_basket):
        num_spins_in_the_last_basket =\
        N_spins - (N_spins/max_n_spins_in_basket)*max_n_spins_in_basket
    else:
        num_spins_in_the_last_basket=0
    ###########################
    samples_matrix=[]
    ## first sample
    numberArray_init = generateNumberArray(N_spins, max_n_spins_in_basket)
    samples_matrix.append(numberArray_init)
    N_sampled = 0
    while N_sampled != N_samples-1 and (N_sampled<2**N_spins):
        #
        ################## update method
        if sampling_method =='update':
            numberArray = updateNumberArray(numberArray_init,
                                            max_n_spins_in_basket, 
                                            num_spins_in_the_last_basket )
        ################## direct
        if sampling_method =='direct':
            numberArray = generateNumberArray(N_spins, max_n_spins_in_basket)
        #################
        #
        if isRepeatedSample(numberArray, samples_matrix)!=0:
            samples_matrix.append(numberArray)
            N_sampled+=1
            numberArray_init = numberArray
    samples_matrix = np.matrix(samples_matrix)
    return samples_matrix , N_sampled


def updateNumberArray(numberArray_init,
                      max_n_spins_in_basket, 
                      num_spins_in_the_last_basket ):
    #
    numberArray_new = np.copy(numberArray_init)
    if num_spins_in_the_last_basket==0:
        col = np.random.randint(len(numberArray_init))
        new_number = np.random.randint(2**max_n_spins_in_basket)
        numberArray_new[col] = new_number
    else:
        col = np.random.randint(len(numberArray_init))
        if col !=len(numberArray_init)-1:
            new_number = np.random.randint(2**max_n_spins_in_basket)
            numberArray_new[col] = new_number
        else:
            new_number = np.random.randint(2**num_spins_in_the_last_basket)
            numberArray_new[col] = new_number
    return numberArray_new
    #
        
        
        
    
#### testing 
#
#args={}
#args['N_spins']=100
#args['max_n_spins_in_basket']=20
#args['N_samples']=10
##M=generateNumberMatrix(**args)
#M = generateNumberMatrix(**args)
#print M[:6, :]
#print M[6:, :]
    