# -*- coding: utf-8 -*-


import numpy as np

def getEnergy2Expectation(energy_hist, beta, E_0,  **args):
    energy_expect=0
    Z=0
    energies=(energy_hist[:, 0]-E_0)
    ####
    for b in range(energy_hist.shape[0]):
        energy = energies[b]
        energy_density = energy_hist[b, 1]
#        print [energy, 
#               energy_density, 
#               np.exp(-beta*energy),
#               Z,
#               energy_expect,
#               ]
        energy_expect+=energy_density * np.exp(-beta*energy)* (energy+E_0)**2
        Z+=energy_density * np.exp(-beta*energy)
    energy_expect = energy_expect/Z
#    print '---------------', energy_expect
    return energy_expect

