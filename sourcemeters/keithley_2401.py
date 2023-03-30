import pyvisa

class keithley_2401:
    def __init__ (self,logger,config):
        '''Opens sourcemeter'''
        try:
            self.rm = pyvisa.ResourceManager()
            self.srcmtr = self.rm.open_resource(config.get('sourcemeter','address'))
            logger.info('Sourcemeter found!')
            self.reset()
        except:
            logger.critical('Sourcemeter not found!')
            quit()
    
    def reset(self):
        '''Resets sourcemeter'''
        self.srcmtr.write('*RST')

    def set_output(self,state):
        '''Sets output state'''
        self.srcmtr.write(f'OUTP {state}')

    def set_current_range(self,range=':AUTO ON'):
        '''Sets current range'''
        self.srcmtr.write(f'SOUR:CURR:RANG{range}')
    
    def set_voltage_range(self,range=':AUTO ON'):
        '''Sets voltage range'''
        self.srcmtr.write(f'SOUR:VOLT:RANG{range}')
    
    def set_fixed_mode(self,mode):
        '''Sets current mode'''
        match mode:
            case 'Current': self.srcmtr.write(f'SOUR:CURR:MODE FIXED')
            case 'Voltage': self.srcmtr.write(f'SOUR:VOLT:MODE FIXED')

    def set_source_function(self,func):
        '''Sets source function'''
        match func:
            case 'Current': self.srcmtr.write('SOUR:FUNC CURR')
            case 'Voltage': self.srcmtr.write('SOUR:FUNC VOLT')

    def set_sense_function(self,func):
        '''Sets sense function'''
        match func:
            case 'Current': self.srcmtr.write('SENS:FUNC "CURR"')
            case 'Voltage': self.srcmtr.write('SENS:FUNC "VOLT"')
            case 'Resistance': self.srcmtr.write('SENS:FUNC "RES"')


    
    def set_current_compliance(self,current):
        '''Sets current compliance'''
        self.srcmtr.write(f'SENS:CURR:PROT {current}')

    def set_voltage(self,voltage):
        '''Sets voltage'''
        self.srcmtr.write(f'SOUR:VOLT:LEV {voltage}')
    
    def set_current(self,current):
        '''Sets current'''
        self.srcmtr.write(f'SOUR:CURR:LEV {current}')
    
    def set_current_nplc(self,nplc):
        '''Sets current integration time'''
        self.srcmtr.write(f'SENS:CURR:NPLC {nplc}')

    def set_voltage_nplc(self,nplc):
        '''Sets voltage integration time'''
        self.srcmtr.write(f'SENS:VOLT:NPLC {nplc}')

    def read(self):
        '''Reads sourcemeter and returns list of values'''
        list_query = self.srcmtr.query(':READ?')[:-1].split(',')
        print (list_query)
        listd_return = []
        for val in list_query:
            listd_return.append(float(val))
        return listd_return

    
    def query(self,command):
        '''Queries sourcemeter'''
        return self.srcmtr.query(command)
    
    def reset_timer(self):
        '''Resets timer'''
        self.srcmtr.write(':SYST:TIME:RES')
    