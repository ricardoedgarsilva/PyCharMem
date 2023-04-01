import time
import numpy as np

class Measurement:
    def __init__(self,logger,config,filesaver):
        
        #Create object variables
        self.config = config
        
        #Read parameters from config file
        self.name = 'pulsedVI'
        self.plot_type = 'twocycles'
        self.necessary_params = ['cycle','n_cycle','v_max','v_min','v_step','v_read','ccplc','t_write','t_read','t_wait','nplc']
        self.result_headers = ['Voltage Write[V]','Current Write [A]','Voltage Read [V]','Current Read [A]', 'Resistance [Ω]', 'Timestamp', 'Time [s]']
        self.params = dict(config.items(f'measurement/{self.name}'))
        #Check if all necessary parameters are present
        check_missing_params(logger,self.params,self.necessary_params)

        #Read parameters
        try:
            logger.info('Reading parameters')
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
            self.nplc   = float(self.params['nplc'])
            logger.info('Parameters read successfully')
        except:
            self.logger.critical('Error reading parameters')
            quit()

        #Create list of voltages
        self.vals = create_list(logger,self.cycle,self.v_max,self.v_min,self.v_step)

        #save config and headers
        filesaver.save_config(logger,config,self.name)
        filesaver.save_headers(self.result_headers)
    
    def set_sourcemeter(self,logger,srcmtr):
        
        #Set sourcemeter to voltage mode
        logger.info('Setting sourcemeter initial parameters')

        try:
            # Set the sourcemeter to autorange mode
            srcmtr.set_source_function(logger,'Voltage')       #Set source mode to voltage
            srcmtr.set_fixed_mode(logger,'Voltage')
            srcmtr.set_current_range(logger)                  #Set current range to autorange
            srcmtr.set_voltage_range(logger)                  #Set voltage range to autorange   
            srcmtr.set_sense_function(logger,'Voltage') #Set sense function to current
            srcmtr.set_sense_function(logger,'Current') #Set sense function to current
            srcmtr.set_current_compliance(logger,self.ccplc) #Set current compliance
            srcmtr.set_current_nplc(logger,self.nplc) #Set sense integration time to 1 PLC
            logger.info('Sourcemeter parameters set successfully')
        except:
            logger.critical('Sourcemeter parameters could not be set')
            quit()

    def measure_cycle(self,logger,srcmtr,plots):

        logger.debug('Starting measurement')
        srcmtr.reset_timer(logger)
        self.result = []
        for val in self.vals:
    
            srcmtr.set_voltage(logger,val)
            srcmtr.set_output(logger,'ON')
            time.sleep(self.t_write)
            result1 = srcmtr.read(logger)           
            srcmtr.set_output(logger,'OFF')

            #wait some time
            time.sleep(self.t_wait)
            
            #read pulse
            srcmtr.set_voltage(logger,self.v_read)
            srcmtr.set_output(logger,'ON')
            time.sleep(self.t_read)
            result2 = srcmtr.read(logger)
            srcmtr.set_output(logger,'OFF')

            # ['Voltage Write[V]','Current Write [A]','Voltage Read [V]','Current Read [A]', 'Resistance [Ω]', 'Timestamp', 'Time [s]']
            self.result.append([result1[0], result1[1], result2[0], result2[1], result2[0]/result2[1], result1[3], timestamp()])
            plots.add_result([result1[0],result1[1],result2[0]/result2[1]])
            plots.update()

        srcmtr.close(logger)
    
        