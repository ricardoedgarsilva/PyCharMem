import pyvisa

class Sourcemeter:
    def __init__ (self, logger, config:dict):
        '''Opens sourcemeter'''
        logger.debug('Initializing sourcemeter...')
        try:
            logger.debug('Looking for sourcemeter...')
            self.rm = pyvisa.ResourceManager()
            self.srcmtr = self.rm.open_resource(config.get('sourcemeter').get('address'))
            logger.debug(f'{config.get("sourcemeter").get("model")} found at {config.get("sourcemeter").get("address")}')
            logger.info('Sourcemeter successfully initialized!')
        except:
            logger.critical('Sourcemeter not found!')
            quit()

#Basic control commands -------------------------------------------------------
    
    def close(self, logger):
        '''Closes sourcemeter'''

        try:
            self.srcmtr.close()
            logger.debug('Sourcemeter closed')
        except:
            logger.critical('Sourcemeter could not be closed! Check GPIB connection!')
            quit()

    def reset(self, logger):
        '''Resets sourcemeter'''
        try:
            self.srcmtr.write('*RST')
            logger.debug('GPIB defaults reseted')
        except:
            logger.critical('GPIB defaults could not reseted! Check GPIB connection!')
            quit()

    def query(self, logger, command:str):
        '''Queries sourcemeter'''
        try:
            query = self.srcmtr.query(command)
            logger.debug(f'Sourcemeter query: {query}')
            return query
        except:
            print('Sourcemeter could not be queried! Check GPIB connection!')
            quit()

    def set_output_state(self, logger, state:str):
        '''Sets output state'''
        try:
            match state:
                case 'ON': self.srcmtr.write('OUTP ON')
                case 'OFF': self.srcmtr.write('OUTP OFF')
            logger.debug(f'Sourcemeter output set to {state}')
        except:
            logger.critical('Sourcemeter output could not be set! Check GPIB connection!')
            quit()

    def set_output_value(self, logger, func:str, value:float):
        '''Sets output value of voltage or current'''
        try:
            match func:
                case 'Current': self.srcmtr.write(f'SOUR:CURR:LEV {value}')
                case 'Voltage': self.srcmtr.write(f'SOUR:VOLT:LEV {value}')
            logger.debug(f'Sourcemeter value set to {value}')
        except:
            logger.critical('Sourcemeter value could not be set! Check GPIB connection!')
            quit()

    def read(self, logger):
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

    def reset_timer(self, logger):
        '''Resets timer'''
        try:
            self.srcmtr.write(':SYST:TIME:RES')
            logger.debug('Sourcemeter timer reseted')
        except:
            logger.critical('Sourcemeter timer could not be reseted! Check GPIB connection!')
            quit()

#Measurement mode commands ------------------------------------------------

    def set_mode_fixed(self, logger, func:str):
        '''Sets fixed mode of voltage or current'''
        try:
            match func:
                case 'Current': self.srcmtr.write(f'SOUR:CURR:MODE FIXED')
                case 'Voltage': self.srcmtr.write(f'SOUR:VOLT:MODE FIXED')
            logger.debug(f'Sourcemeter mode set to {func}')
        except:
            logger.critical('Sourcemeter mode could not be set! Check GPIB connection!')
            quit()

    def set_mode_pulsed(self, logger, func:str):
        '''Sets pulsed mode'''
        try:
            match func:
                case 'Current': self.srcmtr.write(f'SOUR:CURR:MODE PULS')
                case 'Voltage': self.srcmtr.write(f'SOUR:VOLT:MODE PULS')
            logger.debug(f'Sourcemeter pulsed mode set to {func}')
        except:
            logger.critical('Sourcemeter pulsed mode could not be set! Check GPIB connection!')
            quit()

    def set_func_pulse_start(self, logger, func:str, start:float):
        '''Sets pulsed start value'''
        try:
            match func:
                case 'Current': self.srcmtr.write(f'SOUR:CURR:STAR {start}')
                case 'Voltage': self.srcmtr.write(f'SOUR:VOLT:STAR {start}')
            logger.debug(f'Sourcemeter pulsed start set to {start}')
        except:
            logger.critical('Sourcemeter pulsed start could not be set! Check GPIB connection!')
            quit()

    def set_func_pulse_stop(self, logger, func:str, stop:float):
        '''Sets pulsed stop value'''
        try:
            match func:
                case 'Current': self.srcmtr.write(f'SOUR:CURR:STOP {stop}')
                case 'Voltage': self.srcmtr.write(f'SOUR:VOLT:STOP {stop}')
            logger.debug(f'Sourcemeter pulsed stop set to {stop}')
        except:
            logger.critical('Sourcemeter pulsed stop could not be set! Check GPIB connection!')
            quit()

    def set_pulse_delay(self, logger, time:float):
        '''Sets pulsed delay'''
        try:
            self.srcmtr.write(f'SOUR:DEL {time}')
            logger.debug(f'Sourcemeter pulsed delay set to {time}')
        except:
            logger.critical('Sourcemeter pulsed delay could not be set! Check GPIB connection!')
            quit()

    def set_pulse_width(self, logger, time:float):
        '''Sets pulsed width'''
        try:
            self.srcmtr.write(f'SOUR:PULS:WIDT {time}')
            logger.debug(f'Sourcemeter pulsed width set to {time}')
        except:
            logger.critical('Sourcemeter pulsed width could not be set! Check GPIB connection!')
            quit()

#Measurement function commands -------------------------------------------

    def set_src_function(self, logger, func:str):
        '''Sets source function of voltage or current'''
        try:
            match func:
                case 'Current': self.srcmtr.write('SOUR:FUNC CURR')
                case 'Voltage': self.srcmtr.write('SOUR:FUNC VOLT')
            logger.debug(f'Sourcemeter source function set to {func}')
        except:
            logger.critical('Sourcemeter source function could not be set! Check GPIB connection!')
            quit()

    def set_func_range(self, logger, func:str, range:str=':AUTO ON'):
        '''Sets range of voltage or current'''
        try:
            match func:
                case 'Current': self.srcmtr.write(f'SOUR:CURR:RANG {range}')
                case 'Voltage': self.srcmtr.write(f'SOUR:VOLT:RANG {range}')
            logger.debug(f'Sourcemeter range set to {range}')
        except:
            logger.critical('Sourcemeter range could not be set! Check GPIB connection!')
            quit()

    def set_func_step(self, logger, func:str, step:float):
        '''Sets step'''
        try:
            match func:
                case 'Current': self.srcmtr.write(f'SOUR:CURR:STEP {step}')
                case 'Voltage': self.srcmtr.write(f'SOUR:VOLT:STEP {step}')
            logger.debug(f'Sourcemeter step set to {step}')
        except:
            logger.critical('Sourcemeter step could not be set! Check GPIB connection!')
            quit()

    def set_sense_func(self, logger, func:str):
        '''Sets sense function of voltage, current or resistance'''
        try:
            match func:
                case 'Current': self.srcmtr.write('SENS:FUNC "CURR"')
                case 'Voltage': self.srcmtr.write('SENS:FUNC "VOLT"')
                case 'Resistance': self.srcmtr.write('SENS:FUNC "RES"')
            logger.debug(f'Sourcemeter sense function set to {func}')
        except:
            logger.critical('Sourcemeter sense function could not be set! Check GPIB connection!')
            quit()

    def set_func_compliance(self, logger, func:str, value:float):
    
        '''Sets compliance of voltage or current'''
        try:
            match func:
                case 'Current': self.srcmtr.write(f'SENS:CURR:PROT {value}')
                case 'Voltage': self.srcmtr.write(f'SENS:VOLT:PROT {value}')
            logger.debug(f'Sourcemeter compliance set to {value}')
        except:
            logger.critical('Sourcemeter compliance could not be set! Check GPIB connection!')
            quit()

    def set_func_nplc(self, logger, func:str, nplc:float):
        '''Sets integration time for current or voltage'''

        try:
            match func:
                case 'Current': self.srcmtr.write(f'SENS:CURR:NPLC {nplc}')
                case 'Voltage': self.srcmtr.write(f'SENS:VOLT:NPLC {nplc}')
            logger.debug(f'Sourcemeter integration time set to {nplc}')
        except:
            logger.critical('Sourcemeter integration time could not be set! Check GPIB connection!')
            quit()


