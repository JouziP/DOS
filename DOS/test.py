# -*- coding: utf-8 -*-

import numpy as np
#import matplotlib.pyplot as plt

####

### 7000, 5000, 3000
x=[1./7000, 1./5000, 1./3000]
entropy=[0.457,0.466,0.481]
plt.plot(x, entropy, 'o')

z = np.polyfit(x, entropy, 1)
p = np.poly1d(z)
plt.plot(x, entropy, 'o')
plt.plot([0]+x, p([0]+x), '--')