import time
import numpy as np
from modules.common import check_missing_params, create_list, timestamp

class pulsedVI:
    def __init__(self, config, console, logger):
        
        #Create object variables
        self.config = config
        self.console = console
        self.logger = logger
        
        #Read parameters from config file
        self.name = 'pulsedVI'
        self.necessary_params = ['cycle','n_cycle','v_max','v_min','v_step','v_read','ccplc','t_write','t_read','t_wait']
        self.result_headers = ['Voltage Write[V]','Current Write [A]','Voltage Read [V]','Current Read [A]', 'Resistance [Ω]', 'Timestamp', 'Time [s]']
        self.params = dict(config.items(f'measurement/{self.name}'))
        #Check if all necessary parameters are present
        check_missing_params(self.params,self.necessary_params,logger)

        #Read parameters
        try:
            self.logger.info('Reading parameters')
            self.cycle  = self.params['cycle']
            self.n_cycle= int(self.params['n_cycle'])
            self.v_max  = float(self.params['v_max'])
            self.v_min  = float(self.params['v_min'])
            self.v_step = float(self.params['v_step'])
            self.v_read = float(self.params['v_read'])
            self.ccplc  = float(self.params['ccplc'])
            self.t_write= float(self.params['t_write'])
            self.t_read = float(self.params['t_read'])
            self.t_wait = float(self.params['t_wait'])
            self.logger.info('Parameters read successfully')
        except:
            self.logger.critical('Error reading parameters')
            quit()

        #Create list of voltages
        self.vals = create_list(self.cycle,self.v_max,self.v_min,self.v_step,self.logger)
    
    def set_sourcemeter(self, srcmtr):
        
        #Set sourcemeter to voltage mode
        self.logger.info('Setting sourcemeter initial parameters')

        try:
            # Set the sourcemeter to autorange mode
            srcmtr.set_source_function('Voltage') #Set source mode to voltage
            srcmtr.set_fixed_mode('Voltage')
            srcmtr.set_current_range() #Set current range to autorange
            srcmtr.set_voltage_range() #Set voltage range to autorange   
            srcmtr.set_sense_function('Voltage') #Set sense function to current
            srcmtr.set_sense_function('Current') #Set sense function to current
            srcmtr.set_current_compliance(self.ccplc) #Set current compliance
            srcmtr.set_current_nplc(1) #Set sense integration time to 1 PLC
            self.logger.info('Sourcemeter parameters set successfully')
        except:
            self.logger.critical('Sourcemeter parameters could not be set')
            quit()

    def measure_cycle(self,srcmtr):
        srcmtr.reset_timer()
        self.result = []
        for val in self.vals:
    
            srcmtr.set_voltage(val)
            srcmtr.set_output('ON')
            time.sleep(self.t_write)
            result1 = srcmtr.read()           
            srcmtr.set_output('OFF')

            #wait some time
            time.sleep(self.t_wait)
            
            #read pulse
            srcmtr.set_voltage(self.v_read)
            srcmtr.set_output('ON')
            time.sleep(self.t_read)
            result2 = srcmtr.read()
            srcmtr.set_output('OFF')

            # ['Voltage Write[V]','Current Write [A]','Voltage Read [V]','Current Read [A]', 'Resistance [Ω]', 'Timestamp', 'Time [s]']
            self.result.append([result1[0], result1[1], result2[0], result2[1], result2[0]/result2[1], result1[3], timestamp()])

        srcmtr.srcmtr.close()
    
        