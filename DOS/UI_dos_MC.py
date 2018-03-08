# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt

from DOS.FunctionsLayer1.Lattices.latticeConstructor import constructLattice
from FunctionsLayer2.getSampleConfigsEnergysMC import getSampleConfigsEnergysMC
from FunctionsLayer2.getEnergyDist import getEnergyDist
from FunctionsLayer2.getEnergyExpectation import getEnergyExpectation
from FunctionsLayer2.getEnergy2Expectation import getEnergy2Expectation
from FunctionsLayer2.getPartitionFunctionZ import getPartitionFunctionZ

N1=8
N2=8
np.random.seed(1051)
args={}
args['J_const']=1.0
args['E_field']=0.0
args['power']=3.0
#########
a1_x= 1.0
a1_y= 0
theta=np.pi/3
a2_x=np.cos(theta)
a2_y=np.sin(theta)
##
args['a1_x']=a1_x
args['a1_y']=a1_y
args['a2_x']=a2_x
args['a2_y']=a2_y
#########
args['N1'] = N1
args['N2'] = N2
args['N_spins']=N1*N2
args['first_neighb']=True
neighbors_tables_list = constructLattice(**args)
neighbors_table=constructLattice(**args)
args['neighbors_table']=neighbors_table
  
args['max_cluster_size'] = 3

N = N1 * N2
############
args['warm_up_mc_steps']= 5
args['number_of_attempt_2_sample']=20
##
args['E_lower_bound'] =-300
args['E_upper_bound'] =+300
args['num_energy_windows']=200
args['num_sweeps'] =2
#
energys_collected,\
                  configs_collected,\
                      collected_configs_equivalent_decimal=\
                                  getSampleConfigsEnergysMC(**args)
print np.min(energys_collected), np.max(energys_collected), len(energys_collected)
args['num_bins'] = args['num_energy_windows']
energy_hist = getEnergyDist(np.array(energys_collected), **args)
plt.bar(energy_hist[:, 0], energy_hist[:,1])
print energy_hist[0,:]
###########################
Temp_init = 100
Temp_fin = 0.01
num_temp=100
dTemp = (Temp_fin-Temp_init)* 1./num_temp
Temps = [Temp_init + t*dTemp  for t in range(num_temp) ]
Betas = [1./Temp for Temp in Temps]
#############################
energy2_expectation_dt_cumlt = np.zeros([num_temp, 2])
energy_expectation_dt = np.zeros([num_temp, 2])
log_Z_vs_temp=np.zeros([num_temp, 2])
for b in range(num_temp):
        Temp= Temps[b]
#        print Temp
        beta=1./Temp
        log_Z_beta=0
        energy_expct_beta=0
        E_0 = energy_hist[0, 0]
        g_E_0 = 1 #energy_hist[0, 1]
        
        energy_expct_beta=getEnergyExpectation(energy_hist, beta, E_0, **args)*\
        1./(N1*N2)
        energy2_expct_beta=getEnergy2Expectation(energy_hist, beta, E_0, **args)*\
        1./(N1*N2)**2
        ### per spin
        energy_expectation_dt[b, 0]=Temp
        energy_expectation_dt[b, 1]=energy_expct_beta
        energy2_expectation_dt_cumlt[b, 0]=Temp
        energy2_expectation_dt_cumlt[b, 1]=(energy2_expct_beta - energy_expct_beta**2)*\
                            1./Temp**2
        ####
        Z = getPartitionFunctionZ(energy_hist, beta, E_0,g_E_0,  **args)
        log_Z_beta=np.log(Z)
        log_Z_beta=(log_Z_beta) *1./(N1*N2)
        log_Z_vs_temp[b, 0] = Temp
        log_Z_vs_temp[b, 1] = log_Z_beta 
#########
S_vs_beta = np.array([Betas[b]* energy_expectation_dt[b,1] +\
                 log_Z_vs_temp[b, 1] +\
                 -Betas[b]*(E_0)*1./(N1*N2) \
                     for b in range(num_temp)])

discount_fact = np.log(2)/S_vs_beta[0]
S_vs_beta = discount_fact * S_vs_beta
#print S_vs_beta, len(energys_collected)
#########

fig, frame = plt.subplots(3,1, figsize=[10, 10])
frame[0].plot(Temps, energy_expectation_dt[:, 1],
     '-o', label='energy per spin')
frame[1].plot(Temps, energy2_expectation_dt_cumlt[:, 1],
     '-o', label='<E^2>-<E>**2 per spin')
frame[2].plot(Temps, S_vs_beta,
     '-o', label='S per spin')

print S_vs_beta, len(energys_collected)
#plt.hist(energys_collected, 200)
#plt.hist(collected_E_exact_calculation, len(collected_E_exact_calculation))