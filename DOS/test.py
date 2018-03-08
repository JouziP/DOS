from matplotlib.ticker import AutoMinorLocator, MultipleLocator

import matplotlib as mpl
tick_major_font={
                 'labelsize': 16,
                 'size':8,
                 'length':10,
                 'width':2,
                 }   

fig, frame = plt.subplots(3,1, figsize=[10, 10])
frame[0].plot(Temps, energy_expectation_dt[:, 1],
     '-o', label='energy per spin')
frame[1].plot(Temps, energy2_expectation_dt_cumlt[:, 1],
     '-o', label='<E^2>-<E>**2 per spin')
frame[2].plot(Temps, S_vs_beta,
     '-o', label='S per spin')
frame[1].set_xlim([0, 100])
############### tick label size
ml = MultipleLocator(base=2)
frame[1].xaxis.set_major_locator(ml)
#frame[1].tick_params(axis='xaxis', 
#                which='major', 
#                **tick_major_font)
#frame[0].tick_params(axis='both', 
#                which='minor',
#                **tick_minor_font)

print S_vs_beta, len(energys_collected)