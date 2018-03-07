# -*- coding: utf-8 -*-


import numpy as np
#import pandas as pd

#import matplotlib.pyplot as plt

####
from FunctionsLayer1.Lattices.latticeConstructor import constructLattice
from FunctionsLayer2.getSampleEnergyArray_MC import getSampleEnergyArray_MC
from FunctionsLayer2.getEnergyHist import getEnergyHist
from FunctionsLayer2.getEnergyExpectation import getEnergyExpectation
from FunctionsLayer2.getPartitionFunctionZ import getPartitionFunctionZ
####

np.random.seed(1001)
### inputs
N1=8
N2=8
a1_x= 1.0
a1_y= 0
##
theta=np.pi/2
a2_x=np.cos(theta)
a2_y=np.sin(theta)
#####
args={}
args['J_const']=-1.0
args['E_field']=0.0
args['power']=3.0
args['a1_x']=a1_x
args['a1_y']=a1_y
#
args['a2_x']=a2_x
args['a2_y']=a2_y

args['N1'] = N1
args['N2'] = N2
args['N_spins']=N1*N2
args['first_neighb']=True
neighbors_tables_list = constructLattice(**args)
args['neighbors_table']=neighbors_tables_list

### must be a divisor of N1*N2
args['max_n_spins_in_basket']=1 #N1*N2/10
args['N_samples'] = 50
args['N_warm_up']=300
args['num_bins']=args['N_samples']
############################
#Temp_init = 10
#Temp_fin = 0.001
#num_temp=100
#dTemp = (Temp_fin-Temp_init)* 1./num_temp
#Temps = [Temp_init + t*dTemp  for t in range(num_temp) ]
#Betas = [1./Temp for Temp in Temps]
###########################
beta_init = 1
beta_fin = 0.01
num_temp=30
dBeta = (beta_fin-beta_init)* 1./num_temp
Betas = [beta_init + t*dBeta  for t in range(num_temp) ]
Temps = [1./beta for beta in Betas]
Temps.reverse()
Betas.reverse()
##########################
#E_off_set = -100
###########################

log_Z_vs_temp=np.zeros([num_temp, 2])
energy_expectation_dt = np.zeros([num_temp, 2])
scratch=True
for b in range(num_temp):
    Temp= Temps[b]
#    print Temp
    beta=1./Temp
    log_Z_beta=0
    energy_expct_beta=0
    ###############################
    if b!=0: scratch=False
    sampleEnergy_array, args = getSampleEnergyArray_MC(beta, scratch,  **args)
#    print len(sampleEnergy_array)
    energy_hist = getEnergyHist(sampleEnergy_array, **args)
    E_off_set = -128 #np.min(sampleEnergy_array)
#    total_num_samples=len(sampleEnergy_array)
    ###############################
    energy_expct_beta=getEnergyExpectation(energy_hist, beta, E_off_set, **args)*\
    1./(N1*N2)
    ####
    Z = getPartitionFunctionZ(energy_hist, beta, E_off_set, **args)
    #
    log_Z_beta=np.log(Z)
    #
    log_Z_beta=log_Z_beta*1./(N1*N2)- \
        beta*E_off_set/(args['N1']*args['N2'])
    ####
    log_Z_vs_temp[b, 0] = Temp
    log_Z_vs_temp[b, 1] = log_Z_beta 
    ###
    energy_expectation_dt[b, 0]=Temp
    energy_expectation_dt[b, 1]=energy_expct_beta

#######
dLogZ_vs_temp=np.zeros([num_temp-1, 3])
dLogZ_vs_temp[:, 1] = np.array([log_Z_vs_temp[b+1,1 ]-log_Z_vs_temp[b, 1]\
       for b in range(num_temp-1)])
dLogZ_vs_temp[:, 0] = Temps[1:]
#######
dEBeta_vs_temp=np.zeros([num_temp-1, 2])
dEBeta_vs_temp[:, 1]= np.array([ energy_expectation_dt[b+1,1 ]*(1./Temps[b+1])\
                                 - energy_expectation_dt[b,1 ]*(1./Temps[b])
       for b in range(num_temp-1)])
dEBeta_vs_temp[:, 0]=Temps[1:]
#######
#S = [energy_expectation_dt[b,1] *(1./Temps[b]) + log_Z_vs_temp[b,1] for b in range(num_temp) ]
#S  = np.array(S) 
dS = dEBeta_vs_temp[:,1] + dLogZ_vs_temp[:,1] 
S=[np.sum(dS[:t]) for t in range(len(dS)) ]
S= np.array(S) +np.log(2)


###############################################################################
fig, frame = plt.subplots(3,1, figsize=[10, 10])
frame[0].bar(energy_hist[:, 0], energy_hist[:,1])
frame[2].plot(Temps[1:], S, '-o',
     label='entropy per spin - log(2)\nn_sample=%d'%args['N_samples'])
frame[1].plot(Temps, energy_expectation_dt[:, 1],
     '-o', label='energy per spin')
frame[2].legend()
frame[1].legend()