import random
import time

class Instrument:
    def __init__ (self, logger, config):
        """
        Opens and initializes the instrument.

        Parameters
        ----------
        logger : Logger
            the Logger object for logging debug and error messages.
        config : dict
            the configuration parameters for the instrument.
        """

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
        """
        Closes the instrument.

        Parameters
        ----------
        logger : Logger
            the Logger object for logging debug and error messages.
        """

        logger.debug('[SIM] Instrument closed')

    def init(self, logger):
        """
        Initializes the instrument.

        Parameters
        ----------
        logger : Logger
            the Logger object for logging debug and error messages.
        """

        logger.debug('[SIM] Instrument initialized')

    def reset(self, logger):
        """
        Resets the instrument to default settings.

        Parameters
        ----------
        logger : Logger
            the Logger object for logging debug and error messages.
        """

        logger.debug('[SIM] GPIB defaults reseted')

    def write(self, logger, command):
        """
        Writes a command to the instrument.

        Parameters
        ----------
        logger : Logger
            the Logger object for logging debug and error messages.
        command : str
            the command to be written to the instrument.
        """

        logger.debug(f'[SIM] Instrument command: {command}')

    def query(self, logger, command):
        """
        Sends a query to the instrument.

        Parameters
        ----------
        logger : Logger
            the Logger object for logging debug and error messages.
        command : str
            the query to be sent to the instrument.
        """

        logger.debug(f'[SIM] Instrument query: {command}')

    def set_output_state(self, logger, state):
        """
        Sets the output state of the instrument.

        Parameters
        ----------
        logger : Logger
            the Logger object for logging debug and error messages.
        state : str
            the desired state of the instrument output (ON/OFF).
        """
        
        if state == 'ON': self.output_state = True
        elif state == 'OFF': self.output_state = False
        else: logger.critical('[SIM] Invalid output state!')
        logger.debug(f'Instrument output set to {state}')

    def set_output_value(self, logger, func, value):
        """
        Sets the output value for a given function (voltage or current).

        Parameters
        ----------
        logger : Logger
            the Logger object for logging debug and error messages.
        func : str
            the function for which the output value is being set (Voltage/Current).
        value : float
            the desired output value.
        """

        if func == 'Voltage': self.voltage = value
        elif func == 'Current': self.current = value
        else: logger.critical('[SIM] Invalid output function!')

        logger.debug(f'Instrument {func} value set to {value}')

    def get_output_value(self, logger, func):
        """
        Measures the output value for a given function (voltage, current, or resistance).

        Parameters
        ----------
        logger : Logger
            the Logger object for logging debug and error messages.
        func : str
            the function for which the output value is being measured (Voltage/Current/Resistance).
        """
        
        
        # Simulated response based on the function
        if func == 'Voltage': return self.voltage
        elif func == 'Current': return self.current
        elif func == 'Resistance': return self.resistance
        else: logger.critical('[SIM] Invalid output function!')

    def fetch(self, logger):
        """
        Fetches the instrument and returns a list of values.

        Parameters
        ----------
        logger : Logger
            the Logger object for logging debug and error messages.
        """
        
        # Simulated response
        logger.debug('[SIM] Instrument fetched')
        return [self.voltage, self.current, self.resistance ,self.timer]

    def read(self, logger):
        """
        Reads the instrument and returns a list of values.

        Parameters
        ----------
        logger : Logger
            the Logger object for logging debug and error messages.
        """

        # Simulated response
        logger.debug('[SIM] Instrument read')
        return [self.voltage, self.current, self.resistance ,self.timer]

    def get_timer(self, logger):
        """
        Returns the timer value of the instrument.

        Parameters
        ----------
        logger : Logger
            the Logger object for logging debug and error messages.
        """

        # Simulated response
        logger.debug('[SIM] Instrument timer read')
        return self.timer

    def reset_timer(self, logger):
        """
        Resets the timer of the instrument.

        Parameters
        ----------
        logger : Logger
            the Logger object for logging debug and error messages.
        """

        logger.debug('[SIM] Instrument timer reseted')

    # Measurement mode commands ------------------------------------------------

    def set_mode_fixed(self, logger, func):
        """
        Sets the measurement mode of the instrument to 'fixed'.

        Parameters
        ----------
        logger : Logger
            the Logger object for logging debug and error messages.
        func : str
            the function for which the measurement mode is being set.
        """

        logger.debug('[SIM] Instrument measurement mode set to fixed')

    # Measurement function commands -------------------------------------------

    def set_src_func(self, logger, func):
        """
        Sets the source function of the instrument (voltage or current).

        Parameters
        ----------
        logger : Logger
            the Logger object for logging debug and error messages.
        func : str
            the source function to be set on the instrument (Voltage/Current).
        """

        logger.debug(f'[SIM] Instrument source function set to {func}')

    def set_func_range(self, logger, func, range = ':AUTO ON'):
        """
        Sets the range of the given function on the instrument.

        Parameters
        ----------
        logger : Logger
            the Logger object for logging debug and error messages.
        func : str
            the function of the instrument (Voltage/Current).
        range : str
            the range to be set on the instrument (default is ':AUTO ON').
        """

        logger.debug(f'[SIM] Instrument range set to {range}')

    def set_func_step(self, logger, func, step):
        """
        Sets the step for a given function.

        Parameters
        ----------
        logger : Logger
            the Logger object for logging debug and error messages.
        func : str
            the function of the instrument (Voltage/Current).
        step : float
            the step value to be set on the instrument.
        """

        logger.debug(f'[SIM] Instrument step set to {step}')

    def set_sense_func(self, logger, func):
        """
        Sets the sense function of the instrument (voltage, current, or resistance).

        Parameters
        ----------
        logger : Logger
            the Logger object for logging debug and error messages.
        func : str
            the sense function to be set on the instrument (Voltage/Current/Resistance).
        """

        logger.debug(f'[SIM] Instrument sense function set to {func}')

    def set_func_cplc(self, logger, func, value):
        """
        Sets the compliance for a given function (voltage or current).

        Parameters
        ----------
        logger : Logger
            the Logger object for logging debug and error messages.
        func : str
            the function of the instrument (Voltage/Current).
        value : float
            the compliance value to be set on the instrument.
        """

        logger.debug(f'[SIM] Instrument compliance set to {value}')

    def set_func_nplc(self, logger, func, value):
        """
        Sets the integration time for a given function (voltage or current).

        Parameters
        ----------
        logger : Logger
            the Logger object for logging debug and error messages.
        func : str
            the function of the instrument (Voltage/Current).
        value : float
            the integration time to be set on the instrument.
        """

        logger.debug(f'[SIM] Instrument integration time set to {value}')


