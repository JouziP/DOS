# -*- coding: utf-8 -*-

import numpy as np

def generateNumberArray(N_spins, max_n_spins_in_basket):
    num_baskets = (N_spins/max_n_spins_in_basket+1,
                   N_spins/max_n_spins_in_basket)\
                   [N_spins-(N_spins/max_n_spins_in_basket)*\
                    max_n_spins_in_basket==0]
    
#    print num_baskets
#    print [max_n_spins_in_basket for i in range(N_spins/max_n_spins_in_basket)] + [num_spins_in_the_last_basket]
    numberArray=[]
    for q in range(N_spins/max_n_spins_in_basket):
        numberArray.append(np.random.randint(2**(max_n_spins_in_basket) ))
    if num_baskets!=(N_spins/max_n_spins_in_basket):
        num_spins_in_the_last_basket =\
        N_spins - (N_spins/max_n_spins_in_basket)*max_n_spins_in_basket
        numberArray.append(np.random.randint(2**(num_spins_in_the_last_basket)))   
    return numberArray
    
    
    

# testing
#N_spins = 10
#max_n_spins_in_basket=4
#numberArray = generateNumberArray(N_spins, max_n_spins_in_basket)
#print numberArray