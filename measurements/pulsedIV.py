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
    def __init__(self,logger,config,inst):
        '''Set up the measurement'''

        # Set up the measurement parameters
        self.name = 'pulsedIV'
        self.nparams = ['cycle','n_cycles','v+','v-','v_step','v_read','ccplc','t_write','t_read','t_wait','nplc']
        self.headers = ['Voltage Write[V]','Current Write [A]','Voltage Read [V]','Current Read [A]', 'Resistance [Ω]', 'Timer [s]', 'Datetime']
        self.params = dict(config.items())
        self.vals = create_list(
            logger,
            self.params.get(self.name).get('cycle'),
            self.params.get(self.name).get('v+'),
            self.params.get(self.name).get('v-'),
            self.params.get(self.name).get('v_step'))

        #Set up plots parameters
        cycle_type = self.params.get(self.name).get('cycle')
        match len(cycle_type):
            case 1: 
                self.plot_grid = (2,2)
                self.plot_titles = [[f'Cycle I-V {cycle_type}','Resistance vs Time'],
                                    ['Resistance vs Voltage','Voltage vs Time']]
                
                self.plot_labels = [
                    [['Voltage [V]','Current [A]'],
                     ['Time [s]','Resistance [Ω]']],
                    [['Voltage [V]','Resistance [Ω]'],
                     ['Time [s]','Voltage [V]']]]
            case 2:
                self.plot_grid = (2,3)
                self.plot_titles = [['Cycle I-V +','Cycle I-V -','Resistance vs Time'],
                                    ['Resistance vs Voltage +','Resistance vs Voltage -','Voltage vs Time']]
                
                self.plot_labels = [
                    [['Voltage [V]','Current [A]'],['Voltage [V]','Current [A]'],['Time [s]','Resistance [Ω]']],
                    [['Voltage [V]','Resistance [Ω]'],['Voltage [V]','Resistance [Ω]'],['Time [s]','Voltage [V]']]]


        
        # Set up the instrument
        logger.debug('Setting instrument initial parameters')
        
        inst.reset(logger)
        inst.set_mode_fixed(logger, func='Voltage')
        inst.set_src_func(logger,func='Voltage')

        inst.set_sense_func(logger,func='Voltage')
        inst.set_func_range(logger,func='Voltage')

        inst.set_sense_func(logger,func='Current')
        inst.set_func_range(logger,func='Current')
        inst.set_func_ccplc(logger,func='Current',value=self.params.get(self.name).get('ccplc'))
        inst.set_func_nplc(logger,func='Current',value=self.params.get(self.name).get('nplc'))
        #Prepare the instrument for measurements
        inst.write(logger,'INIT:IMM')

        logger.debug('Instrument parameters set!')

    
    def measure_val(self,logger,console,inst,val):

        # Write Pulse: Start
        time.sleep(self.params.get(self.name).get('t_wait'))
        inst.set_output_value(logger,'Voltage',val)
        time.sleep(self.params.get(self.name).get('t_write'))
        resultwrite = inst.read(logger)
        # Write Pulse: End

        time.sleep(self.params.get(self.name).get('t_wait'))

        # Read Pulse: Start
        inst.set_output_value(logger,'Voltage',self.params.get(self.name).get('v_read'))
        time.sleep(self.params.get(self.name).get('t_read'))
        resultread = inst.read(logger)
        # Read Pulse: End

        return([
                resultwrite[0], # Voltage Write
                resultwrite[1], # Current Write
                resultread[0], # Voltage Read
                resultread[1], # Current Read
                resultread[0]/resultread[1], # Resistance
                resultread[3], # Timer write
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) # Timestamp computer
                ])



        


        