# -*- coding: utf-8 -*-


import numpy as np

def getEnergyExpectation(energy_hist, beta,  **args):
    energy_expect=0
    Z=0
    for b in range(energy_hist.shape[0]):
        energy = energy_hist[b, 0]
        energy_density = energy_hist[b, 1]
        energy_expect+=energy_density * np.exp(-beta*energy)* energy
        Z+=energy_density * np.exp(-beta*energy)
    energy_expect = energy_expect/Z
    return energy_expect



#### test
#import matplotlib.pyplot as plt
#from DOS.FunctionsLayer1.Lattices.latticeConstructor import constructLattice
#from DOS.FunctionsLayer2.getSampleEnergyArray import getSampleEnergyArray
#from DOS.FunctionsLayer2.getEnergyHist import getEnergyHist
#np.random.seed(1201)
#N1=6
#N2=6
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
#args['first_neighb']=True
#neighbors_tables_list = constructLattice(**args)
#args['neighbors_table']=neighbors_tables_list
#
#args['max_n_spins_in_basket']=N1*N2/3
#args['N_samples']=500
#
#np.random.seed(1212)
#Temp_init = 10
#Temp_fin = 0.1
#num_temp=20
#dTemp = (Temp_fin-Temp_init)* 1./num_temp
#Temps = [Temp_fin - t*dTemp  for t in range(num_temp) ]
#Betas = [1./Temp for Temp in Temps]
#num_avg=5
#energy_expectation_dt = np.zeros([num_temp, 2])
#for b in range(0,num_temp):
#    Temp= Temps[b]
#    beta=1./Temp
#    energy_expct_beta=0
#    for s in range(num_avg):
#        sampleEnergy_array = getSampleEnergyArray(**args)
#        ###
#        args['num_bins']=500
#        ##energy_array = np.array([-50, -40,-2,0,0 ,1, 2, -12, -19])
#        energy_hist = getEnergyHist(sampleEnergy_array, **args)
#        ####
#        energy_expct_beta+=getEnergyExpectation(energy_hist, beta, **args)*\
#        1./(N1*N2)*1./num_avg
#        #
#    energy_expectation_dt[b, 0]=Temp
#    energy_expectation_dt[b, 1]=energy_expct_beta
#    
#
#dE_vs_temp=np.zeros([num_temp-1, 2])
#dE_vs_temp[:, 1]= np.array([energy_expectation_dt[b+1,1 ]- energy_expectation_dt[b, 1]\
#       for b in range(num_temp-1)])
#dE_vs_temp[:, 0]=Temps[1:]
#plt.plot(Temps[1:], dE_vs_temp[:,1], '-o')
#
#    
#    
#    
#    
