# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

####
from FunctionsLayer1.Lattices.latticeConstructor import constructLattice
from FunctionsLayer2.getSampleEnergyArray import getSampleEnergyArray
from FunctionsLayer2.getEnergyDist import getEnergyDist
from FunctionsLayer2.getEnergyExpectation import getEnergyExpectation
from FunctionsLayer2.getPartitionFunctionZ import getPartitionFunctionZ
####

np.random.seed(1001)
### inputs
N1=4
N2=4
a1_x= 1.0
a1_y= 0
##
theta=np.pi/2
a2_x=np.cos(theta)
a2_y=np.sin(theta)
###########
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

args['max_n_spins_in_basket']=1 #N1*N2/10
args['N_samples']=400
args['num_bins']=args['N_samples']
###########################
### choice of Numeraire:
#args['Numeraire']='spot'
args['Numeraire']='terminal'
###########################
## update or direct
args['sampling_method'] = 'direct'
###########################
Temp_init = 10
Temp_fin = 0.001
num_temp=40
dTemp = (Temp_fin-Temp_init)* 1./num_temp
Temps = [Temp_init + t*dTemp  for t in range(num_temp) ]
Betas = [1./Temp for Temp in Temps]
#############################
#beta_init = 20
#beta_fin = 0.001
#num_temp=200
#dBeta = (beta_fin-beta_init)* 1./num_temp
#Betas = [beta_init + t*dBeta  for t in range(num_temp) ]
#Temps = [1./beta for beta in Betas]
#Temps.reverse()
#Betas.reverse()
########################### 
num_replica = 1
energy_expectation_vs_t_adjusted= np.zeros([num_temp, 2])
S_vs_beta= np.zeros([num_temp, 2])

for m in range(num_replica):
    print m
    sampleEnergy_array, N_sampled = getSampleEnergyArray(**args)
#    print N_sampled
    ###
    energy_hist = getEnergyDist(sampleEnergy_array, **args)
    ################
    log_Z_vs_temp=np.zeros([num_temp, 2])
    energy_expectation_dt = np.zeros([num_temp, 2])
    for b in range(num_temp):
        Temp= Temps[b]
#        print Temp
        beta=1./Temp
        log_Z_beta=0
        energy_expct_beta=0
        ###############################
        if args['Numeraire']=='spot':
            E_0 = np.min(sampleEnergy_array)
        if args['Numeraire']=='terminal':
            adjust=16
            E_0 = -16+adjust
        ###############################
        energy_expct_beta=getEnergyExpectation(energy_hist, beta, E_0, **args)*\
        1./(N1*N2)
        ####
        Z = getPartitionFunctionZ(energy_hist, beta, E_0, **args)
        #
        log_Z_beta=np.log(Z)
    #    log_Z_0_beta= np.log(Z_0)
        #
        log_Z_beta=(log_Z_beta) *1./(N1*N2)
    #    log_Z_0_beta=log_Z_0_beta*1./(N1*N2)
        ####
        ### per spin
        log_Z_vs_temp[b, 0] = Temp
        log_Z_vs_temp[b, 1] = log_Z_beta 
    #    log_Z_vs_temp[b, 2] = log_Z_0_beta
        ### per spin
        energy_expectation_dt[b, 0]=Temp
        energy_expectation_dt[b, 1]=energy_expct_beta
    
    #################
    ## S - S_0
    
    S_vs_beta[:, 1] += np.array([Betas[b]* energy_expectation_dt[b,1] +\
                 log_Z_vs_temp[b, 1] +\
                 -Betas[b]*(E_0)
                 \
                 for b in range(num_temp)])/num_replica
    
    energy_expectation_vs_t_adjusted[:, 1] += (energy_expectation_dt[:,1]-\
                                            E_0*1./(N1*N2))/num_replica
    ###############################################################################
#
#OutputFolder='./OUTPUTS/'
##### S
#filename='S_N1_%d_N2_%d_N_samples_%d_N_bins_%d_basket_%d_1stNN_%r_J_%d.csv'\
#%(args['N1'],
#  args['N2'],
#  args['N_samples'],
#  args['num_bins'],
#  args['max_n_spins_in_basket'],
#  args['first_neighb'],
#  args['J_const']
#  )
#S_df = pd.DataFrame(S)
#S_df.to_csv(OutputFolder+filename)
#S_df.index=Temps[1:]
##### Energy_avg
#filename='E_N1_%d_N2_%d_N_samples_%d_N_bins_%d_basket_%d_1stNN_%r_J_%d.csv'\
#%(args['N1'],
#  args['N2'],
#  args['N_samples'],
#  args['num_bins'],
#  args['max_n_spins_in_basket'],
#  args['first_neighb'],
#  args['J_const']
#  )
#E_df = pd.DataFrame(energy_expectation_dt[:, 1])
#E_df.to_csv(OutputFolder+filename)
#E_df.index=Temps
##### Hist
#filename='Hist_N1_%d_N2_%d_N_samples_%d_N_bins_%d_basket_%d_1stNN_%r_J_%d.csv'\
#%(args['N1'],
#  args['N2'],
#  args['N_samples'],
#  args['num_bins'],
#  args['max_n_spins_in_basket'],
#  args['first_neighb'],
#  args['J_const']
#  )
#energy_hist_df= pd.DataFrame(energy_hist)
#energy_hist_df.to_csv(OutputFolder+filename)
#
#
#
#
#
#


###############################################################################
fig, frame = plt.subplots(3,1, figsize=[10, 10])
frame[0].hist(sampleEnergy_array, len(sampleEnergy_array))
frame[2].plot(Temps, S_vs_beta[:,1], '-o',
     label='entropy per spin - Z_0\nn_sample=%d'%args['N_samples'])
frame[1].plot(Temps, energy_expectation_dt[:, 1],
     '-o', label='energy per spin')
frame[2].legend()
frame[1].legend()


