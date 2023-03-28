import time
import numpy as np
from modules.common_utils import check_missing_params

class Measurement:
    def __init__(self, config, console, logger):
        #Read configuration file
        
        self.name = 'pulsed'
        self.necessary_params = ['cycle','n_cycle','v_max','v_min','v_step','v_read','t_write','t_read','t_wait']
        self.params = dict(config.items(f'measurement/{self.name}'))

        #Check if all necessary parameters are present
        check_missing_params(self.params,self.necessary_params,logger)

    def measure(self, sourcemeter, config):
        #Read parameters
        cycle = self.params['cycle']
        n_cycle = int(self.params['n_cycle'])
        v_max = float(self.params['v_max'])
        v_min = float(self.params['v_min'])
        v_step = float(self.params['v_step'])
        v_read = float(self.params['v_read'])
        t_write = float(self.params['t_write'])
        t_read = float(self.params['t_read'])
        t_wait = float(self.params['t_wait'])


        #Set sourcemeter to voltage mode
        sourcemeter.write('SOUR:FUNC VOLT')         #Set source function to voltage
        sourcemeter.write('SOUR:VOLT:MODE FIXED')   #Set source mode to fixed
        sourcemeter.write('SOUR:VOLT:RANG 10')      #Set source range to 10V
        sourcemeter.write('SOUR:VOLT:LEV 0')        #Set source level to 0V
        sourcemeter.write('SOUR:VOLT:ILIM 0.1')     #Set source current limit to 100mA
        sourcemeter.write('SOUR:VOLT:STAT ON')      #Turn source on
        sourcemeter.write('SENS:FUNC "CURR"')       #Set sense function to current
        sourcemeter.write('SENS:CURR:PROT 0.1')     #Set sense current protection to 100mA
        sourcemeter.write('SENS:CURR:RANG 0.1')     #Set sense current range to 100mA
        sourcemeter.write('SENS:CURR:NPLC 1')       #Set sense integration time to 1 PLC
        sourcemeter.write('SENS:CURR:STAT ON')      #Turn sense on
        sourcemeter.write('OUTP OFF')               #Turn output off

        #Create voltage lists for each cycle
        vlistp  =   np.concatenate((np.arange(0, v_max+v_step, v_step), np.arange(v_max-v_step, -v_step, -v_step)))
        vlistn  =   np.concatenate((np.arange(0, v_min-v_step, -v_step), np.arange(v_min+v_step, v_step, v_step)))
        
        match cycle:
            case '+':   voltage_list = vlistp
            case '-':   voltage_list = vlistn
            case '+-':  voltage_list = np.concatenate(vlistp,vlistn)
            case '-+':  voltage_list = np.concatenate(vlistn,vlistp)

        #Create lists to store data
        voltage_write = []
        current_write = []
        voltage_read = []
        current_read = []

        for cycle_i in range(n_cycle):
            for voltage_val in voltage_list:



def measure_pulsed(sourcemeter,config):



        #Create voltage lists for each cycle
    vlistp  =   np.concatenate((np.arange(0, v_max+v_step, v_step), np.arange(v_max-v_step, -v_step, -v_step)))
    vlistn  =   np.concatenate((np.arange(0, v_min-v_step, -v_step), np.arange(v_min+v_step, v_step, v_step)))
    
    match cycle:
        case '+':   voltage_list = vlistp
        case '-':   voltage_list = vlistn
        case '+-':  voltage_list = np.concatenate(vlistp,vlistn)
        case '-+':  voltage_list = np.concatenate(vlistn,vlistp)


    for cycle_i in range(n_cycle):
        for voltage_val in voltage_list:
            #write pulse
            sourcemeter.write('SOUR:VOLT {}'.format(voltage_val))
            sourcemeter.write('OUTP ON')
            time.sleep(t_write)
            current_write = sourcemeter.query('MEAS:CURR?')
            sourcemeter.write('OUTP OFF')

            #wait some time
            time.sleep(t_wait)
            
            #read pulse
            sourcemeter.write('SOUR:VOLT {}'.format(v_read))
            sourcemeter.write('OUTP ON')
            time.sleep(t_read)
            current_read = sourcemeter.query('MEAS:CURR?')
            sourcemeter.write('OUTP OFF')

    sourcemeter.close()