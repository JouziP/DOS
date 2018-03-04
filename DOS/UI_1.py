# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

####
from DOS.FunctionsLayer1.Lattices.latticeConstructor import constructLattice
from DOS.FunctionsLayer2.getSampleEnergyArray import getSampleEnergyArray
from DOS.FunctionsLayer2.getEnergyHist import getEnergyHist
from DOS.FunctionsLayer2.getEnergyExpectation import getEnergyExpectation
from DOS.FunctionsLayer2.getPartitionFunctionZ import getPartitionFunctionZ
####

np.random.seed(1201)
### inputs
N1=6
N2=6

args={}
args['J_const']=1.0
args['E_field']=0.0
args['power']=3.0
args['a1_x']=1.0
args['a1_y']=0.0
#
args['a2_x']=0.0
args['a2_y']=1.0

args['N1'] = N1
args['N2'] = N2
args['N_spins']=N1*N2
args['first_neighb']=True
neighbors_tables_list = constructLattice(**args)
args['neighbors_table']=neighbors_tables_list

args['max_n_spins_in_basket']=N1*N2/3
args['N_samples']=200
args['num_bins']=200
###########################
Temp_init = 2
Temp_fin = 0.1
num_temp=100
num_avg=20
###########################
dTemp = (Temp_fin-Temp_init)* 1./num_temp
Temps = [Temp_fin - t*dTemp  for t in range(num_temp) ]
Betas = [1./Temp for Temp in Temps]

log_Z_vs_temp=np.zeros([num_temp, 2])
energy_expectation_dt = np.zeros([num_temp, 2])
for b in range(num_temp):
    Temp= Temps[b]
    beta=1./Temp
    log_Z_beta=0
    energy_expct_beta=0
    for s in range(num_avg):
        sampleEnergy_array = getSampleEnergyArray(**args)
        ###
        energy_hist = getEnergyHist(sampleEnergy_array, **args)
        ####
        log_Z_beta+=np.log(getPartitionFunctionZ(energy_hist, beta, **args))
        log_Z_beta=log_Z_beta*1./(N1*N2)*1./num_avg
        ####
        energy_expct_beta+=getEnergyExpectation(energy_hist, beta, **args)*\
        1./(N1*N2)*1./num_avg
        ####
    ####
    log_Z_vs_temp[b, 0] = Temp
    log_Z_vs_temp[b, 1] = log_Z_beta
    ####
    energy_expectation_dt[b, 0]=Temp
    energy_expectation_dt[b, 1]=energy_expct_beta


#######
dLogZ_vs_temp=np.zeros([num_temp-1, 2])
dLogZ_vs_temp[:, 1]= np.array([log_Z_vs_temp[b+1,1 ]-log_Z_vs_temp[b, 1]\
       for b in range(num_temp-1)])
dLogZ_vs_temp[:, 0]=Temps[1:]
#######
dE_vs_temp=np.zeros([num_temp-1, 2])
dE_vs_temp[:, 1]= np.array([energy_expectation_dt[b+1,1 ]- energy_expectation_dt[b, 1]\
       for b in range(num_temp-1)])
dE_vs_temp[:, 0]=Temps[1:]

dS = dE_vs_temp[:,1] + dLogZ_vs_temp[:,1]
fig, frame = plt.subplots(2,1, figsize=[10, 10])
frame[0].plot(Temps[1:], dS[:]+np.log(2), '-o', label='entropy per spin - log(2)')
frame[1].plot(Temps, energy_expectation_dt[:, 1], '-o', label='energy per spin')
frame[0].legend()
frame[1].legend()


