# -*- coding: utf-8 -*-

import numpy as np

from DOS.BasicFunctions.generateNumberArray import generateNumberArray


def getSampleMatrix_unique(**args):
    M = generateNumberMatrix(**args)
    M_checker=M
    
    num_repeated_samples=0
    for row_1 in range(M_checker.shape[0]-1):
        for row_2 in range(row_1+1, M_checker.shape[0]):
            col=0
            
            if M_checker[row_1, col]==M_checker[row_2, col]:
                counter=1
                for col in range(1, M_checker.shape[1]):
                    if M_checker[row_1, col]==M_checker[row_2, col]:
                        counter+=1
                if counter==M_checker.shape[1]:
                    num_repeated_samples+=1
                    print row_1, row_2
    return num_repeated_samples, M
                



#
def generateNumberMatrix(**args):
    N_spins = args['N_spins']
    max_n_spins_in_basket = args['max_n_spins_in_basket']
    N_samples = args['N_samples']
    samples_matrix=[]
    for s in range(N_samples):
        samples_matrix.append(generateNumberArray(N_spins, max_n_spins_in_basket))
    samples_matrix = np.matrix(samples_matrix)
    
    return samples_matrix
        
    
#### testing 

args={}
args['N_spins']=4
args['max_n_spins_in_basket']=2
args['N_samples']=10
#M=generateNumberMatrix(**args)
n, M=getSampleMatrix_unique(**args)
print n
print M
    