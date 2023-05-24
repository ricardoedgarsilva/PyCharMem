import random
import time

class Instrument:
    def __init__ (self, logger, config:dict):
        '''Opens instrument'''
        logger.warning('THIS IS A SIMULATED INSTRUMENT, NO HARDWARE IS BEING USED! "[SIM]" WILL BE PRINTED BEFORE ALL LOGS')
        logger.debug('[SIM] Initializing instrument...')
        self.voltage = 1.0
        self.current = 1e-3
        self.resistance = 1000.0
        self.timer = 0.0
        self.output_state = False
        logger.info('[SIM] Instrument successfully initialized!')


    # Basic control commands -------------------------------------------------------
    
    def close(self, logger):
        '''Closes instrument'''
        logger.debug('[SIM] Instrument closed')

    def init(self, logger):
        '''Initializes instrument'''
        logger.debug('[SIM] Instrument initialized')

    def reset(self, logger):
        '''Resets instrument'''
        logger.debug('[SIM] GPIB defaults reseted')

    def write(self, logger, command: str):
        '''Writes command to instrument'''
        logger.debug(f'[SIM] Instrument command: {command}')

    def query(self, logger, command: str):
        '''Queries instrument'''
        logger.debug(f'[SIM] Instrument query: {command}')

    def set_output_state(self, logger, state: str):
        '''Sets output state'''
        if state == 'ON': self.output_state = True
        elif state == 'OFF': self.output_state = False
        else: logger.critical('[SIM] Invalid output state!')
        logger.debug(f'Instrument output set to {state}')

    def set_output_value(self, logger, func: str, value: float):
        '''Sets output value of voltage or current'''
        if func == 'Voltage': self.voltage = value
        elif func == 'Current': self.current = value
        else: logger.critical('[SIM] Invalid output function!')

        logger.debug(f'Instrument {func} value set to {value}')

    def get_output_value(self, logger, func: str):
        '''Measures output value of voltage, current, or resistance'''
        # Simulated response based on the function
        if func == 'Voltage': return self.voltage
        elif func == 'Current': return self.current
        elif func == 'Resistance': return self.resistance
        else: logger.critical('[SIM] Invalid output function!')

    def fetch(self, logger):
        '''Fetches instrument and returns list of values'''
        # Simulated response
        logger.debug('[SIM] Instrument fetched')
        return [self.voltage, self.current, self.resistance ,self.timer]

    def read(self, logger):
        '''Reads instrument and returns list of values'''
        # Simulated response
        logger.debug('[SIM] Instrument read')
        return [self.voltage, self.current, self.resistance ,self.timer]

    def get_timer(self, logger):
        '''Returns timer value'''
        # Simulated response
        logger.debug('[SIM] Instrument timer read')
        return self.timer

    def reset_timer(self, logger):
        '''Resets timer'''
        logger.debug('[SIM] Instrument timer reseted')

    # Measurement mode commands ------------------------------------------------

    def set_mode_fixed(self, logger, func: str):
        '''Sets measurement mode to fixed'''
        logger.debug('[SIM] Instrument measurement mode set to fixed')

    # Measurement function commands -------------------------------------------

    def set_src_func(self, logger, func: str):
        '''Sets source function of voltage or current'''
        logger.debug(f'[SIM] Instrument source function set to {func}')

    def set_func_range(self, logger, func: str, range: str = ':AUTO ON'):
        '''Sets range of voltage or current'''
        logger.debug(f'[SIM] Instrument range set to {range}')

    def set_func_step(self, logger, func: str, step: float):
        '''Sets step'''
        logger.debug(f'[SIM] Instrument step set to {step}')

    def set_sense_func(self, logger, func: str):
        '''Sets sense function of voltage, current, or resistance'''
        logger.debug(f'[SIM] Instrument sense function set to {func}')

    def set_func_cplc(self, logger, func: str, value: float):
        '''Sets compliance of voltage or current'''
        logger.debug(f'[SIM] Instrument compliance set to {value}')

    def set_func_nplc(self, logger, func: str, value: float):
        '''Sets integration time for current or voltage'''
        logger.debug(f'[SIM] Instrument integration time set to {value}')
