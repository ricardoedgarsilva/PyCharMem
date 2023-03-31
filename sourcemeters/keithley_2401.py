import pyvisa

class Sourcemeter:
    def __init__ (self,logger,config):
        '''Opens sourcemeter'''
        try:
            logger.debug('Looking for sourcemeter...')
            self.rm = pyvisa.ResourceManager()
            self.srcmtr = self.rm.open_resource(config.get('sourcemeter','address'))
            logger.debug(f'{config.get("sourcemeter","model")} found at {config.get("sourcemeter","address")}')
            logger.info('Sourcemeter successfully initialized!')
            self.reset()
        except:
            logger.critical('Sourcemeter not found!')
            quit()
    
    def reset(self,logger):
        '''Resets sourcemeter'''
        try:
            self.srcmtr.write('*RST')
            logger.debug('GPIB defaults reseted')
        except:
            logger.critical('GPIB defaults could not reseted! Check GPIB connection!')
            quit()

    def set_output(self,logger,state):
        '''Sets output state'''
        try:
            self.srcmtr.write(f'OUTP {state}')
            logger.debug(f'Sourcemeter output set to {state}')
        except:
            logger.critical('Sourcemeter output could not be set! Check GPIB connection!')
            quit()

    def set_current_range(self,logger,range=':AUTO ON'):
        '''Sets current range'''
        try:
            self.srcmtr.write(f'SOUR:CURR:RANG{range}')
            logger.debug(f'Sourcemeter current range set to {range}')
        except:
            logger.critical('Sourcemeter current range could not be set! Check GPIB connection!')
            quit()
    
    def set_voltage_range(self,logger,range=':AUTO ON'):
        '''Sets voltage range'''
        try:
            self.srcmtr.write(f'SOUR:VOLT:RANG{range}')
            logger.debug(f'Sourcemeter voltage range set to {range}')
        except:
            logger.critical('Sourcemeter voltage range could not be set! Check GPIB connection!')
            quit()

    def set_fixed_mode(self,logger,mode):
        '''Sets current mode'''
        try:
            match mode:
                case 'Current': self.srcmtr.write(f'SOUR:CURR:MODE FIXED')
                case 'Voltage': self.srcmtr.write(f'SOUR:VOLT:MODE FIXED')
            logger.debug(f'Sourcemeter mode set to {mode}')
        except:
            logger.critical('Sourcemeter mode could not be set! Check GPIB connection!')
            quit()

    def set_source_function(self,logger,func):
        '''Sets source function'''
        try:
            match func:
                case 'Current': self.srcmtr.write('SOUR:FUNC CURR')
                case 'Voltage': self.srcmtr.write('SOUR:FUNC VOLT')
            logger.debug(f'Sourcemeter source function set to {func}')
        except:
            logger.critical('Sourcemeter source function could not be set! Check GPIB connection!')
            quit()

    def set_sense_function(self,logger,func):
        '''Sets sense function'''
        try:
            match func:
                case 'Current': self.srcmtr.write('SENS:FUNC "CURR"')
                case 'Voltage': self.srcmtr.write('SENS:FUNC "VOLT"')
                case 'Resistance': self.srcmtr.write('SENS:FUNC "RES"')
            logger.debug(f'Sourcemeter sense function set to {func}')
        except:
            logger.critical('Sourcemeter sense function could not be set! Check GPIB connection!')
            quit()
    
    def set_current_compliance(self,logger,current):
        '''Sets current compliance'''
        try:
            self.srcmtr.write(f'SENS:CURR:PROT {current}')
            logger.debug(f'Sourcemeter current compliance set to {current}')
        except:
            logger.critical('Sourcemeter current compliance could not be set! Check GPIB connection!')
            quit()

    def set_voltage(self,logger,voltage):
        '''Sets voltage'''
        try:
            self.srcmtr.write(f'SOUR:VOLT:LEV {voltage}')
            logger.debug(f'Sourcemeter voltage set to {voltage}')
        except:
            logger.critical('Sourcemeter voltage could not be set! Check GPIB connection!')
            quit()
    
    def set_current(self,logger,current):
        '''Sets current'''
        try:
            self.srcmtr.write(f'SOUR:CURR:LEV {current}')
            logger.debug(f'Sourcemeter current set to {current}')
        except:
            logger.critical('Sourcemeter current could not be set! Check GPIB connection!')
            quit()

    def set_current_nplc(self,logger,nplc):
        '''Sets current integration time'''
        try:
            self.srcmtr.write(f'SENS:CURR:NPLC {nplc}')
            logger.debug(f'Sourcemeter current integration time set to {nplc}')
        except:
            logger.critical('Sourcemeter current integration time could not be set! Check GPIB connection!')
            quit()

    def set_voltage_nplc(self,logger,nplc):
        '''Sets voltage integration time'''
        try:
            self.srcmtr.write(f'SENS:VOLT:NPLC {nplc}')
            logger.debug(f'Sourcemeter voltage integration time set to {nplc}')
        except:
            logger.critical('Sourcemeter voltage integration time could not be set! Check GPIB connection!')
            quit()

    def read(self,logger):
        '''Reads sourcemeter and returns list of values'''
        try:
            list_query = self.srcmtr.query(':READ?')[:-1].split(',')
            logger.debug(f'Sourcemeter read: {list_query}')
            listd_return = []
            for val in list_query:
                listd_return.append(float(val))
            return listd_return
        except:
            print('Sourcemeter could not be read! Check GPIB connection!')
            quit()

    def query(self,logger,command):
        '''Queries sourcemeter'''
        try:
            query = self.srcmtr.query(command)
            logger.debug(f'Sourcemeter query: {query}')
            return query
        except:
            print('Sourcemeter could not be queried! Check GPIB connection!')
            quit()
    
    def reset_timer(self,logger):
        '''Resets timer'''
        try:
            self.srcmtr.write(':SYST:TIME:RES')
            logger.debug('Sourcemeter timer reseted')
        except:
            logger.critical('Sourcemeter timer could not be reseted! Check GPIB connection!')
            quit()

    