# -*- coding: utf-8 -*-


import numpy as np

def generateNumberArray(N_spins, max_number):
    num_baskets = (N_spins/max_number+1,
                   N_spins/max_number)[N_spins -(N_spins/max_number)*max_number==0]
    
    num_spins_in_the_last_basket =  N_spins - (N_spins/max_number)*max_number
    print num_baskets
    print [max_number for i in range(N_spins/max_number)] + [num_spins_in_the_last_basket]
    numberArray=[]
    for q in range(N_spins/max_number):
        numberArray.append(np.random.randint(2**(max_number) ))
    numberArray.append(np.random.randint(2**(num_spins_in_the_last_basket)) )
    return numberArray
    
    
    

## testing
#N_spins = 10
#max_number=6
#numberArray = generateNumberArray(N_spins, max_number)
#print numberArray