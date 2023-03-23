import pyvisa
import configparser
import numpy as np

# configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# open sourcemeter
rm = pyvisa.ResourceManager()
sourcemeter = rm.open_resource(config.get('sourcemeter','address'))


def save():
    pass


def measurement_pulsed():

    #Read configuration file
    cycle   =   config.getint('measurementVI','cycle')
    t_write =   config.getfloat('measurementVI/pulsed','t_write')
    t_read  =   config.getfloat('measurementVI/pulsed','t_read')
    t_wait  =   config.getfloat('measurementVI/pulsed','t_wait')
    n_cycle =   config.getint('measurementVI/pulsed','n_cycle')
    v_read  =   config.getfloat('measurementVI/pulsed','v_read')
    v_step  =   config.getfloat('measurementVI/pulsed','v_step')
    v_max   =   config.getfloat('measurementVI/pulsed','v_max')
    v_min   =   config.getfloat('measurementVI/pulsed','v_min')


    match cycle:
        case '+':  
            voltage_list = np.concatenate((np.arange(0, v_max+v_step, v_step), np.arange(v_max-v_step, -v_step, -v_step)))
        case '-':
            voltage_list = voltage_list = np.concatenate((np.arange(0, v_min-v_step, -v_step), np.arange(v_min, v_step, v_step)))
        case '+-':
            listp = 
        

    for cycle in range(n_cycle):






        for voltage_val in np.concatenate((np.arange(0, end+step, step), np.arange(end-step, -step, -step))):









# Set voltage level to 1 V
keithley.write('SOUR:VOLT 1')

# Turn on output
keithley.write('OUTP ON')

# Measure current
current = keithley.query('MEAS:CURR?')

# Turn off output
keithley.write('OUTP OFF')

keithley.close()
