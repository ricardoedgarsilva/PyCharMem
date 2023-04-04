import time
import numpy as np

def create_list(logger,cycle,max,min,step):
    '''Creates a list of values'''
    import numpy as np

    list1 = np.arange(0,max,step)
    listp = np.concatenate((list1,np.array([max]),np.flip(list1)))

    list2 = np.arange(0,min,-step)
    listn = np.concatenate((list2,np.array([min]),np.flip(list2)))

    try:
        match cycle:
            case '+': return listp
            case '-': return listn
            case '+-': return np.concatenate((listp,listn))
            case '-+': return np.concatenate((listn,listp))
    except:
        logger.critical('Invalid cycle type!')
        quit()


class Measurement:
    def __init__(self,logger,config,srcmtr):
        '''Set up the measurement'''

        # Set up the measurement parameters
        self.name = 'pulsedIV'
        self.plot_file = 'twocycles'
        self.nparams = ['cycle','n_cycle','v_max','v_min','v_step','v_read','ccplc','t_write','t_read','t_wait','nplc']
        self.headers = ['Voltage Write[V]','Current Write [A]','Voltage Read [V]','Current Read [A]', 'Resistance [Ω]', 'Timestamp', 'Time [s]']
        self.params = dict(config.items(self.name))
        # Create voltage values
        self.vals = create_list(logger,
                                self.params.get(self.name).get('cycle'),
                                self.params.get(self.name).get('v_max'),
                                self.params.get(self.name).get('v_min'),
                                self.params.get(self.name).get('v_step'))


        logger.debug('Measurement parameters set!')

        # Set up the sourcemeter
        logger.debug('Setting sourcemeter initial parameters')
        
        try:
            # Set the sourcemeter to autorange mode
            srcmtr.reset() 
            srcmtr.set_mode_fixed(logger, func='Voltage')
            srcmtr.set_source_function(logger,func='Voltage')
            srcmtr.set_measurement_function(logger,func='Voltage')
            srcmtr.set_measurement_function(logger,func='Current')
            srcmtr.set_measurement_range(logger,func='Current')
            srcmtr.set_measurement_range(logger,func='Voltage')
            srcmtr.set_ccplc(logger,ccplc=self.params.get(self.name).get('ccplc'))
            logger.info('Sourcemeter parameters set successfully')
        except:
            logger.critical('Sourcemeter parameters could not be set')
            quit()

    
    def measure_cycle(self,logger,console,srcmtr,plots,filesave):

        logger.debug('Starting measurement')
        srcmtr.reset_timer(logger)
        self.result = []

        for val in self.vals:
    
            time.sleep(self.params.get(self.name).get('t_wait'))
            srcmtr.set_output_value(logger,'Voltage',val)
            srcmtr.set_output_state(logger,'ON')
            time.sleep(self.params.get(self.name).get('t_write'))
            srcmtr.set_output_state(logger,'OFF')
            result1 = srcmtr.read(logger)
            time.sleep(self.params.get(self.name).get('t_wait'))
            srcmtr.set_output_value(logger,'Voltage',self.params.get(self.name).get('v_read'))
            srcmtr.set_output_state(logger,'ON')
            time.sleep(self.params.get(self.name).get('t_read'))
            srcmtr.set_output_state(logger,'OFF')
            result2 = srcmtr.read(logger)

            self.result.append([
                result1[0], # Voltage Write
                result1[1], # Current Write
                result2[0], # Voltage Read
                result2[1], # Current Read
                result2[0]/result2[1], # Resistance
                result1[3], # Timestamp write
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) # Timestamp computer
                ])
            
            print(self.result[-1]) # Temporary print to console

            filesave.save_result(self.result[-1])
            
            plots.add_result([result1[0],result1[1],result2[0]/result2[1]])
            plots.update()

        srcmtr.close(logger)
    
        