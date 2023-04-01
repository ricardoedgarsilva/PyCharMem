#import test_data.lvm as csv and save each line as a list in a list

import csv
import numpy as np
from plots.twocycles import Plots
import time
import matplotlib.pyplot as plt


with open('test_data.lvm', 'r') as f:
    #import values as floats
    reader = csv.reader(f, delimiter='\t')
    data = list(reader)


data = np.array(data)

plt.ion()
plots = Plots()

for i in range(1, 50):
    plots.add_result([float(data[i,1]), float(data[i,2]), float(data[i,4])])
    plots.update()



plots.show()

