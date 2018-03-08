# -*- coding: utf-8 -*-


import numpy as np

def getPartitionFunctionZ(energy_hist, beta, E_0,g_E_0,  **args):
    Z=0
    #### subtract the min energy from all energies:   
#    Z_0 = np.exp(-beta*(energy_expct_beta*args['N1'] *args['N2']) )
#    Z_0 = np.exp(-beta*( energy_hist[0,0]) ) 
    #####
#    E_0 = energy_hist[0,0]
#    E_0=0
#    sigma  = energy_hist[-1,0]  - energy_hist[0,0]
    sigma=1
#    E_0=+args['N1']*args['N2']*.8
    energies=(energy_hist[:, 0]-E_0)/sigma
    ####
    for b in range(energy_hist.shape[0]):
        energy = energies[b]
        energy_density = energy_hist[b, 1]
#        print energy_density * np.exp(-beta*energy)
        Z+=energy_density * np.exp(-beta*energy)
    return Z*1./g_E_0



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
#log_Z_vs_temp=np.zeros([num_temp, 2])
##entrop_vs_temp[0, :]=np.array([Temp, S])
#for b in range(num_temp):
#    Temp= Temps[b]
#    beta=1./Temp
#    log_Z_beta=0
#    for s in range(num_avg):
#        sampleEnergy_array = getSampleEnergyArray(**args)
#        ###
#        args['num_bins']=500
#        ##energy_array = np.array([-50, -40,-2,0,0 ,1, 2, -12, -19])
#        energy_hist = getEnergyHist(sampleEnergy_array, **args)
##        plt.bar(energy_hist[:,0], energy_hist[:,1])
#        ####
#        log_Z_beta+=np.log(getPartitionFunctionZ(energy_hist, beta, **args))
#        log_Z_beta=log_Z_beta*1./(N1*N2)*1./num_avg
#    log_Z_vs_temp[b, 0] = Temp
#    log_Z_vs_temp[b, 1] = log_Z_beta
#    
#    
#dLogZ_vs_temp=np.zeros([num_temp-1, 2])
#dLogZ_vs_temp[:, 1]= np.array([log_Z_vs_temp[b+1,1 ]-log_Z_vs_temp[b, 1]\
#       for b in range(num_temp-1)])
#dLogZ_vs_temp[:, 0]=Temps[1:]
#plt.plot(Temps[1:], dLogZ_vs_temp[:,1], '-o')