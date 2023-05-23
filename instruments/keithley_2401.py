import pyvisa

class Instrument:
    def __init__ (self, logger, config:dict):
        '''Opens instrument'''
        logger.debug('Initializing instrument...')
        try:
            logger.debug('Looking for instrument...')
            self.rm = pyvisa.ResourceManager()
            self.inst = self.rm.open_resource(config.get('instrument').get('address'))
            logger.debug(f'{config.get("instrument").get("model")} found at {config.get("instrument").get("address")}')
            logger.info('Instrument successfully initialized!')
        except:
            logger.critical('Instrument not found!')
            quit()

#Basic control commands -------------------------------------------------------
    
    def close(self, logger):
        '''Closes instrument'''

        try:
            self.inst.close()
            logger.debug('Instrument closed')
        except:
            logger.critical('Instrument could not be closed! Check connection!')
            quit()

    def init(self,logger):
        '''Initializes instrument'''
        try:
            self.inst.write('INIT')
            logger.debug('Instrument initialized')
        except:
            logger.critical('Instrument could not be initialized! Check connection!')
            quit()

    def reset(self, logger):
        '''Resets instrument'''
        try:
            self.inst.write('*RST')
            logger.debug('GPIB defaults reseted')
        except:
            logger.critical('GPIB defaults could not reseted! Check connection!')
            quit()

    def write(self, logger, command:str):
        '''Writes command to instrument'''
        try:
            self.inst.write(command)
            logger.debug(f'Instrument command: {command}')
        except:
            print('Instrument could not be written! Check connection!')
            quit()

    def query(self, logger, command:str):
        '''Queries instrument'''
        try:
            query = self.inst.query(command)
            logger.debug(f'Instrument query: {query}')
            return query
        except:
            print('Instrument could not be queried! Check connection!')
            quit()

    def set_output_state(self, logger, state:str):
        '''Sets output state'''
        try:
            match state:
                case 'ON': self.inst.write('OUTP ON')
                case 'OFF': self.inst.write('OUTP OFF')
            logger.debug(f'Instrument output set to {state}')
        except:
            logger.critical('Instrument output could not be set! Check connection!')
            quit()

    def set_output_value(self, logger, func:str, value:float):
        '''Sets output value of voltage or current'''
        try:
            match func:
                case 'Current': self.inst.write(f'SOUR:CURR:LEV {value}')
                case 'Voltage': self.inst.write(f'SOUR:VOLT:LEV {value}')
            logger.debug(f'Instrument value set to {value}')
        except:
            logger.critical('Instrument value could not be set! Check connection!')
            quit()

    def get_output_value(self, logger, func:str):
        '''Measures output value of voltage, current or resistance'''
        #try:
        match func:
            case 'Current': 
                out = self.inst.query('MEAS:CURR?').split(',')[1]
            case 'Voltage': 
                out = self.inst.query('MEAS:VOLT?').split(',')[0]
            case 'Resistance': 
                out = self.inst.query('MEAS:RES?').split(',')[2]
        #except:
        #    logger.critical('Instrument value could not be measured! Check connection!')
        #    quit()

    def fetch(self, logger):
        '''Fetches instrument and returns list of values'''
        try:
            list_query = self.inst.query('FETC?')[:-1].split(',')
            logger.debug(f'Instrument fetch: {list_query}')
            listd_return = []
            for val in list_query:
                listd_return.append(float(val))
            return listd_return
        except:
            print('Instrument could not be fetched! Check connection!')
            quit()

    def read(self, logger):
        '''Reads instrument and returns list of values'''
        try:
            list_query = self.inst.query('READ?')[:-1].split(',')
            logger.debug(f'Instrument read: {list_query}')
            listd_return = []
            for val in list_query:
                listd_return.append(float(val))
            return listd_return
        except:
            print('Instrument could not be read! Check connection!')
            quit()

    def get_timer(self,logger):
        '''Returns timer value'''
        try:
            timer = self.inst.query(':SYST:TIME?')
            return float(timer)
        except:
            logger.critical('Instrument timer could not be read! Check connection!')
            quit()

    def reset_timer(self, logger):
        '''Resets timer'''
        try:
            self.inst.write(':SYST:TIME:RES')
            logger.debug('Instrument timer reseted')
        except:
            logger.critical('Instrument timer could not be reseted! Check connection!')
            quit()

#Measurement mode commands ------------------------------------------------

    def set_mode_fixed(self, logger , func:str):
        '''Sets measurement mode to fixed'''
        try:
            match func:
                case 'Current': self.inst.write('SOUR:CURR:MODE FIXED')
                case 'Voltage': self.inst.write('SOUR:VOLT:MODE FIXED')
            logger.debug('Instrument measurement mode set to fixed')
        except:
            logger.critical('Instrument measurement mode could not be set! Check connection!')
            quit()

#Measurement function commands -------------------------------------------

    def set_src_func(self, logger, func:str):
        '''Sets source function of voltage or current'''
        try:
            match func:
                case 'Current': self.inst.write('SOUR:FUNC CURR')
                case 'Voltage': self.inst.write('SOUR:FUNC VOLT')
            logger.debug(f'Instrument source function set to {func}')
        except:
            logger.critical('Instrument source function could not be set! Check connection!')
            quit()

    def set_func_range(self, logger, func:str, range:str=':AUTO ON'):
        '''Sets range of voltage or current'''
        try:
            match func:
                case 'Current': self.inst.write(f'SOUR:CURR:RANG{range}')
                case 'Voltage': self.inst.write(f'SOUR:VOLT:RANG{range}')
                case 'Resistance': self.inst.write(f'SOUR:RES:RANG{range}')
            logger.debug(f'Instrument range set to {range}')
        except:
            logger.critical('Instrument range could not be set! Check connection!')
            quit()

    def set_func_step(self, logger, func:str, step:float):
        '''Sets step'''
        try:
            match func:
                case 'Current': self.inst.write(f'SOUR:CURR:STEP {step}')
                case 'Voltage': self.inst.write(f'SOUR:VOLT:STEP {step}')
            logger.debug(f'Instrument step set to {step}')
        except:
            logger.critical('Instrument step could not be set! Check connection!')
            quit()

    def set_sense_func(self, logger, func:str):
        '''Sets sense function of voltage, current or resistance'''
        try:
            match func:
                case 'Current': self.inst.write('SENS:FUNC "CURR"')
                case 'Voltage': self.inst.write('SENS:FUNC "VOLT"')
                case 'Resistance': self.inst.write('SENS:FUNC "RES"')
            logger.debug(f'Instrument sense function set to {func}')
        except:
            logger.critical('Instrument sense function could not be set! Check connection!')
            quit()

    def set_func_ccplc(self, logger, func:str, value:float):
    
        '''Sets compliance of voltage or current'''
        try:
            match func:
                case 'Current': self.inst.write(f'SENS:CURR:PROT {value}')
                case 'Voltage': self.inst.write(f'SENS:VOLT:PROT {value}')
            logger.debug(f'Instrument compliance set to {value}')
        except:
            logger.critical('Instrument compliance could not be set! Check connection!')
            quit()

    def set_func_nplc(self, logger, func:str, value:float):
        '''Sets integration time for current or voltage'''

        try:
            match func:
                case 'Current': self.inst.write(f'SENS:CURR:NPLC {value}')
                case 'Voltage': self.inst.write(f'SENS:VOLT:NPLC {value}')
            logger.debug(f'Instrument integration time set to {value}')
        except:
            logger.critical('Instrument integration time could not be set! Check connection!')
            quit()


