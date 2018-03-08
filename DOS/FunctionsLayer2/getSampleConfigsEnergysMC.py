# -*- coding: utf-8 -*-


import numpy as np

from DOS.BasicFunctions.getRandomConfig import getRandomConfig

from DOS.FunctionsLayer1.getEnergyOfSpinConfig import getEnergyOfConfig  

from DOS.FunctionsLayer2.updateCluster import updateCluster

def getSampleConfigsEnergysMC(**args):
    N1 = args['N1']
    N2 = args['N2']
    N = N1 * N2
    #### ####### energy windows:
    ## ex. num_energy_windows = 100
    num_energy_windows=args['num_energy_windows']
    ## ex. E_lower_bound= -10
    E_lower_bound = args['E_lower_bound']
    ## ex. E_lower_bound= 40
    E_upper_bound = args['E_upper_bound']
    ## ex. dE = (40 - (-10) )/100 = 0.5
    dE = (E_upper_bound - E_lower_bound)*1./num_energy_windows
    ## ex. E_marks = 40, 40 -.5 ,..., 40 - 0.5*100=-10
    E_marks=[E_upper_bound - dE*i for i in range(num_energy_windows+1)]
    for loop in range(args['num_sweeps']):
        E_marks +=[E_lower_bound + dE*i for i in range(num_energy_windows+1)]
        E_marks +=[E_upper_bound - dE*i for i in range(num_energy_windows+1)]
    
    
    #### ######## init configs:
    config_current = getRandomConfig(N)
    idxs_current = [i for i in range(N)]
    E_current  = getEnergyOfConfig(config_current, **args)
    ####
    warm_up_mc_steps = args['warm_up_mc_steps']
    number_of_attempt_2_sample = args['number_of_attempt_2_sample']
    collected_configs_equivalent_decimal=[]
    energys_collected = []
    configs_collected=[]
    #### for BM
#    collected_E_exact_calculation=[]
#    E_current_bm = E_current
#    collected_E_exact_calculation.append(E_current_bm)
    ####
    count = 0
    for E_mark in E_marks:
        count+=1
        if count >= 1*num_energy_windows: 
            rule=2
        else:
            rule=1
        for i in range(warm_up_mc_steps):
            config_current,\
            idxs_current,\
            E_current,\
            dE_2add= updateCluster(config_current, 
                                 idxs_current, 
                                 E_current,
                                 E_mark,
                                 N,  
                                 rule,
                                 **args)
#            E_current_bm = getEnergyOfConfig(config_current, **args)
#            print np.round(E_current_bm,5)==np.round(E_current,5)
        ####
        for s in range(number_of_attempt_2_sample):
            ## warm - up
            for i in range(warm_up_mc_steps):
                config_current,\
                idxs_current,\
                E_current,\
                dE_2add= updateCluster(config_current, 
                                     idxs_current, 
                                     E_current,
                                     E_mark,
                                     N,  
                                     rule,
                                     **args)
#                E_current_bm = getEnergyOfConfig(config_current, **args)
#                print np.round(E_current_bm,5)==np.round(E_current,5)
            ## collect
            decimal_config , config_binarry= getDecimalEquivalent(config_current)
            if decimal_config not in collected_configs_equivalent_decimal:
                energys_collected.append(E_current)
                configs_collected.append(config_current)
                collected_configs_equivalent_decimal.append(decimal_config)
#                collected_E_exact_calculation.append(E_current_bm)
    #####
    return energys_collected,\
                  configs_collected,\
                      collected_configs_equivalent_decimal#,\
#                          collected_E_exact_calculation
                      
#########################################################################    
def getDecimalEquivalent(config_current):
    equiv_decimal=0
    config_binarry = [(0, 1)[config_current[i]==-1] \
                      for i in range(len(config_current))]
    for i in range(len(config_binarry)):
        equiv_decimal +=(2**i)*config_binarry[i]
    return equiv_decimal, config_binarry


###### test getDecimalEquivalent
#N = 4
#config_current = getRandomConfig(N)
#equiv_decimal, config_binarry = getDecimalEquivalent(config_current)
#print config_current, config_binarry ,  equiv_decimal


####### test
#from DOS.FunctionsLayer1.Lattices.latticeConstructor import constructLattice
##import matplotlib.pyplot as plt
#N1=3
#N2=3
#np.random.seed(1051)
#args={}
#args['J_const']=1.0
#args['E_field']=0.0
#args['power']=3.0
##########
#a1_x= 1.0
#a1_y= 0
#theta=np.pi/3
#a2_x=np.cos(theta)
#a2_y=np.sin(theta)
###
#args['a1_x']=a1_x
#args['a1_y']=a1_y
#args['a2_x']=a2_x
#args['a2_y']=a2_y
##########
#args['N1'] = N1
#args['N2'] = N2
#args['N_spins']=N1*N2
#args['first_neighb']=False
#neighbors_tables_list = constructLattice(**args)
#neighbors_table=constructLattice(**args)
#args['neighbors_table']=neighbors_table
#  
#args['max_cluster_size'] = 3
#
#N = N1 * N2
#############
#args['warm_up_mc_steps']= 5
#args['number_of_attempt_2_sample']=10
###
#args['E_lower_bound'] =-30
#args['E_upper_bound'] =+50
#args['num_energy_windows']=100
#args['num_sweeps'] = 2
###
#energys_collected,\
#                  configs_collected,\
#                      collected_configs_equivalent_decimal=\
#                                  getSampleConfigsEnergysMC(**args)
#print np.min(energys_collected), np.max(energys_collected), len(energys_collected)
#
#import matplotlib.pyplot as plt
#plt.hist(energys_collected, 200)
##plt.hist(collected_E_exact_calculation, len(collected_E_exact_calculation))