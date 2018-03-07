# -*- coding: utf-8 -*-

import numpy as np


def clusterLattice(**args):
    N_spins = args['N_spins']
    N_spins_in_basket = args['max_n_spins_in_basket']
    
    num_baskets = N_spins/N_spins_in_basket
    clusters = [[i+c*N_spins_in_basket for i in range(N_spins_in_basket)] 
                                            for c in range(num_baskets)]
    if num_baskets*N_spins_in_basket!=N_spins:
        last_cluster=[i for i in range(num_baskets*N_spins_in_basket, 
                                       N_spins)]
        clusters.append(last_cluster)
    return clusters
                
                
        
        






##### test
from DOS.FunctionsLayer1.Lattices.latticeConstructor import constructLattice
N1=2
N2=4

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
args['first_neighb']=False
neighbors_tables_list = constructLattice(**args)
neighbors_table=constructLattice(**args)
args['neighbors_table']=neighbors_table

args['max_n_spins_in_basket']=5
clusterLattice(**args)
