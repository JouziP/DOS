# -*- coding: utf-8 -*-


import numpy as np

def getEnergyOfConfig(sampleSpinConfig, **args):
    neighbors_table=args['neighbors_table']
    J_const =args['J_const']
    E_field =args['E_field']
    energy_total=0
#    print sampleSpinConfig.shape
    for spin_idx in range(len(sampleSpinConfig)):
        spin_neighbors=neighbors_table[spin_idx]
        ####### energy of the spin:
        S = sampleSpinConfig[spin_idx]
        spin_energy = E_field*S
        for n in range(spin_neighbors.shape[0]):
            neighb_idx=spin_neighbors[n,  0]
            strength  = spin_neighbors[n, 1]   
            S_n = sampleSpinConfig[int(neighb_idx)]
#            print S_n
            spin_energy += (J_const*(strength)) * (S*S_n)
#        print spin_energy
            
        energy_total+=spin_energy
    energy_total=energy_total/float(2)
    return energy_total
            
            
        
    
    