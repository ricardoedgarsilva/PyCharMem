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
        self.plot_type = 'IVcycles'
        self.nparams = ['cycle','n_cycles','v_start','v_stop','v_step','v_read','ccplc','t_write','t_read','t_wait','nplc']
        self.headers = ['Voltage Write[V]','Current Write [A]','Voltage Read [V]','Current Read [A]', 'Resistance [Ω]', 'Timer [s]', 'Datetime']
        self.params = dict(config.items())
        # Create voltage values
        self.vals = create_list(logger,
                                self.params.get(self.name).get('cycle'),
                                self.params.get(self.name).get('v_start'),
                                self.params.get(self.name).get('v_stop'),
                                self.params.get(self.name).get('v_step'))


        logger.debug('Measurement parameters set!')

        # Set up the sourcemeter
        logger.debug('Setting sourcemeter initial parameters')

        
        # Set the sourcemeter to autorange mode
        srcmtr.reset(logger)
        srcmtr.set_mode_fixed(logger, func='Voltage')
        srcmtr.set_src_func(logger,func='Voltage')
        srcmtr.set_sense_func(logger,func='Voltage')
        srcmtr.set_sense_func(logger,func='Current')
        srcmtr.set_func_range(logger,func='Current')
        srcmtr.set_func_range(logger,func='Voltage')
        srcmtr.set_func_ccplc(logger,func='Current',value=self.params.get(self.name).get('ccplc'))
        srcmtr.set_func_nplc(logger,func='Current',value=self.params.get(self.name).get('nplc'))
        logger.info('Sourcemeter parameters set successfully')


    
    def measure_cycle(self,logger,console,srcmtr,plots,filesave):

        logger.debug('Starting measurement')
        srcmtr.reset_timer(logger)
        self.result = []

        for val in self.vals:
    

            time.sleep(self.params.get(self.name).get('t_wait'))
            srcmtr.set_output_value(logger,'Voltage',val)
            srcmtr.set_output_state(logger,'ON')
            time.sleep(self.params.get(self.name).get('t_write'))
            v_write = val
            i_write = srcmtr.get_output_value(logger,'Current')
            srcmtr.set_output_state(logger,'OFF')
            
            time.sleep(self.params.get(self.name).get('t_wait'))
            srcmtr.set_output_value(logger,'Voltage',self.params.get(self.name).get('v_read'))
            srcmtr.set_output_state(logger,'ON')
            time.sleep(self.params.get(self.name).get('t_read'))
            v_read = srcmtr.get_output_value(logger,'Voltage')
            i_read = srcmtr.get_output_value(logger,'Current')
            resist = srcmtr.get_output_value(logger,'Resistance')
            srcmtr.set_output_state(logger,'OFF')
            timer = srcmtr.get_timer(logger)
            

            self.result.append([
                v_write, # Voltage Write
                i_write, # Current Write
                v_read, # Voltage Read
                i_read, # Current Read
                resist, # Resistance
                timer, # Timer write
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) # Timestamp computer
                ])
            
            print(self.result[-1]) # Temporary print to console

            filesave.save_result(logger,self.result[-1])
            
            plots.add_result([v_write,i_write,v_read,timer])
            plots.update()

        
    
        