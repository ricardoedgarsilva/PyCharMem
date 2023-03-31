#import test_data.lvm as csv and save each line as a list in a list

import csv
import numpy as np
from modules.interface import measurement_plots
import time
import matplotlib.pyplot as plt


with open('test_data.lvm', 'r') as f:
    #import values as floats
    reader = csv.reader(f, delimiter='\t')
    data = list(reader)


data = np.array(data)

plt.ion()
plots = measurement_plots()

for i in range(1, 100):
    plots.add_result([float(data[i,1]), float(data[i,2]), float(data[i,4])])
    plots.update()



plots.show()

