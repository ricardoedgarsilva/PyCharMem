import numpy as np

cycle = '+'
v_max = 3 + 1e-5
v_min = -3 - 1e-5
v_step = 2.7



vlistp  =   np.concatenate((np.arange(0, v_max, v_step), np.arange(v_max-v_step, -v_step, -v_step)))
vlistn  =   np.concatenate((np.arange(0, v_min, -v_step), np.arange(v_min+v_step, v_step, v_step)))

match cycle:
    case '+':   voltage_list = vlistp
    case '-':   voltage_list = vlistn
    case '+-':  voltage_list = np.concatenate(vlistp,vlistn)
    case '-+':  voltage_list = np.concatenate(vlistn,vlistp)

print(voltage_list)
