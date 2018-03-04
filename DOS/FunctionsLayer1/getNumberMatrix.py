# -*- coding: utf-8 -*-

import numpy as np

from DOS.BasicFunctions.generateNumberArray import generateNumberArray


def isRepeatedSample(samples_matrix):
    num_repeated_samples=0
    for row_1 in range(samples_matrix.shape[0]-1):
        for row_2 in range(row_1+1, samples_matrix.shape[0]):
            col=0
            if samples_matrix[row_1, col]==samples_matrix[row_2, col]:
                counter=1
                for col in range(1, samples_matrix.shape[1]):
                    if samples_matrix[row_1, col]==samples_matrix[row_2, col]:
                        counter+=1
                if counter==samples_matrix.shape[1]:
                    num_repeated_samples+=1
                    print row_1, row_2
    return (True, False)[num_repeated_samples==0]    
#
def generateNumberMatrix(**args):
    N_spins = args['N_spins']
    max_n_spins_in_basket = args['max_n_spins_in_basket']
    N_samples = args['N_samples']
    ##
    samples_matrix=[]
    for s in range(N_samples):
        samples_matrix.append(generateNumberArray(N_spins, max_n_spins_in_basket))
    samples_matrix = np.matrix(samples_matrix)
    ##
    n_attmpt=0
    _tolerance = 100
    while isRepeatedSample(samples_matrix)==True and n_attmpt<_tolerance: 
        samples_matrix=[]
        for s in range(N_samples):
            samples_matrix.append(generateNumberArray(N_spins, max_n_spins_in_basket))
        samples_matrix = np.matrix(samples_matrix)
        ##
        n_attmpt+=1
        print n_attmpt
    return samples_matrix

        
    
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
    