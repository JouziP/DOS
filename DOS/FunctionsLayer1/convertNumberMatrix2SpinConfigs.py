# -*- coding: utf-8 -*-

import numpy as np


from DOS.BasicFunctions.getBinaryArray import getBinaryArray

def convertNumberMatrix2SpinConfigs(samples_matrix, 
                                    **args):
    N_spins = args['N_spins']
    max_n_spins_in_basket = args['max_n_spins_in_basket']
    N_samples = samples_matrix.shape[0]
    ################
    num_baskets = (N_spins/max_n_spins_in_basket+1,
                   N_spins/max_n_spins_in_basket)\
                   [N_spins-(N_spins/max_n_spins_in_basket)*\
                    max_n_spins_in_basket==0]
    if num_baskets!=(N_spins/max_n_spins_in_basket):
        num_spins_in_the_last_basket =\
        N_spins - (N_spins/max_n_spins_in_basket)*\
                max_n_spins_in_basket
        numSpinsInBasket_array = []
        for p in range(N_spins/max_n_spins_in_basket):
            numSpinsInBasket_array.append(max_n_spins_in_basket)
        numSpinsInBasket_array.append(num_spins_in_the_last_basket)
    else:
        numSpinsInBasket_array = []
        for p in range(N_spins/max_n_spins_in_basket):
            numSpinsInBasket_array.append(max_n_spins_in_basket)
    ################
    sampleSpinConfigsMatrix=np.zeros([N_samples, N_spins], dtype=int)
    for row in range(samples_matrix.shape[0]):
        binaryArray=[]
        for col in range(samples_matrix.shape[1]):
            n=samples_matrix[row, col]
            binaryArray_local=getBinaryArray(numSpinsInBasket_array[col],n)
            binaryArray+=binaryArray_local
#            print binaryArray
        ################################ assumes S={+1, -1}
        binaryArray = [(-1)**b for b in binaryArray]
        ################################ !!!!!!!!!!!!!!!!!
        sampleSpinConfigsMatrix[row, :] = np.array(binaryArray)
    return sampleSpinConfigsMatrix
    
### testing 
#from getNumberMatrix import generateNumberMatrix
##
#args={}
#args['N_spins']=5
#args['max_n_spins_in_basket']=3
#args['N_samples']=4
#M = generateNumberMatrix(**args)
#sampleSpinConfigsMatrix =convertNumberMatrix2SpinConfigs(M, 
#                                    **args)  
#print sampleSpinConfigsMatrix
