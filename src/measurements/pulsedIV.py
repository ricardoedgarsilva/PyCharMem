import time
import numpy as np

def create_list(logger, cycle, max_val, min_val, step):
    """
    Create a list of values based on the specified cycle type and parameters.

    Args:
        logger (logging.Logger): The logger object to use for logging messages.
        cycle (str): The cycle type. Valid values are '+', '-', '+-', '-+'.
        max_val (float): The maximum value for the list.
        min_val (float): The minimum value for the list.
        step (float): The step size between consecutive values.

    Returns:
        numpy.ndarray: The generated list of values, rounded to 5 decimal places.

    Raises:
        ValueError: If the cycle type is invalid.

    """

    list_positive = np.concatenate((np.arange(0, max_val, step), [max_val], np.flip(np.arange(0, max_val, step))))
    list_negative = np.concatenate((np.arange(0, min_val, -step), [min_val], np.flip(np.arange(0, min_val, -step))))

    try:
        match cycle:
            case '+': return np.round(list_positive,5)
            case '-': return np.round(list_negative,5)
            case '+-': return np.round((np.concatenate((list_positive, list_negative))),5)
            case '-+': return np.round(np.concatenate((list_negative, list_positive)),5)
    except:
        logger.critical('Invalid cycle type!')
        quit()

class Measurement:
    def __init__(self, logger, config, instrument):
        """
        Initialize a Measurement object.

        Args:
            logger (logging.Logger): The logger object to use for logging messages.
            config (dict): The configuration dictionary containing measurement parameters.
            instrument (object): The instrument object used for measurement.

        """

        self.name = 'pulsedIV'
        self.nparams = ['cycle', 'n_cycles', 'v+', 'v-', 'v_step', 'v_read', 'ccplc+', 'ccplc-', 't_write', 't_read', 't_wait', 'nplc']
        self.headers = ['Voltage Write[V]', 'Current Write [A]', 'Voltage Read [V]', 'Current Read [A]', 'Resistance [Ω]', 'Timer [s]', 'Datetime']
        self.params = dict(config.items())
        self.vals = create_list(
            logger,
            self.params.get(self.name).get('cycle'),
            self.params.get(self.name).get('v+'),
            self.params.get(self.name).get('v-'),
            self.params.get(self.name).get('v_step'))
        self.set_plot_parameters(self.params.get(self.name).get('cycle'))
        self.initialize_instrument(logger, instrument)

    def set_plot_parameters(self, cycle_type):
        """
        Set the plot parameters based on the cycle type.

        Args:
            cycle_type (str): The cycle type.

        """
        match len(cycle_type):
            case 1: 
                self.plot_grid = (2, 2)
                self.plot_titles = [[f'Cycle I-V {cycle_type}', 'Resistance vs Time'],
                                    ['Resistance vs Voltage', 'Voltage vs Time']]
                self.plot_labels = [
                    [['Voltage [V]', 'Current [A]'],
                     ['Time [s]', 'Resistance [Ω]']],
                    [['Voltage [V]', 'Resistance [Ω]'],
                     ['Time [s]', 'Voltage [V]']]]
                self.plot_clear = [[True, False], [True, False]]
            case 2:
                self.plot_grid = (2, 3)
                self.plot_titles = [['Cycle I-V +', 'Cycle I-V -', 'Resistance vs Time'],
                                    ['Resistance vs Voltage +', 'Resistance vs Voltage -', 'Voltage vs Time']]
                self.plot_labels = [
                    [['Voltage [V]', 'Current [A]'], ['Voltage [V]', 'Current [A]'], ['Time [s]', 'Resistance [Ω]']],
                    [['Voltage [V]', 'Resistance [Ω]'], ['Voltage [V]', 'Resistance [Ω]'], ['Time [s]', 'Voltage [V]']]]
                self.plot_clear = [[True, True, False], [True, True, False]]

    def initialize_instrument(self, logger, instrument):
        """
        Initialize the instrument with the specified parameters.

        Args:
            logger (logging.Logger): The logger object to use for logging messages.
            instrument (object): The instrument object used for measurement.

        """

        logger.debug('Setting instrument initial parameters')
        instrument.reset(logger)
        instrument.set_mode_fixed(logger, func='Voltage')
        instrument.set_src_func(logger, func='Voltage')
        instrument.set_sense_func(logger, func='Voltage')
        instrument.set_func_range(logger, func='Voltage')
        instrument.set_sense_func(logger, func='Current')
        instrument.set_func_range(logger, func='Current')
        instrument.set_func_nplc(logger, func='Current', value=self.params.get(self.name).get('nplc'))
        #instrument.write(logger, 'INIT:IMM')
        logger.debug('Instrument parameters set!')

    def measure_val(self, logger, instrument, val):
        """
        Perform a measurement for a specific value.

        Args:
            logger (logging.Logger): The logger object to use for logging messages.
            instrument (object): The instrument object used for measurement.
            val (float): The value to measure.

        Returns:
            list: The measurement results and plots.

        """

        if val>0: instrument.set_func_cplc(logger, func="Current", value=self.params.get(self.name).get('ccplc+'))
        else: instrument.set_func_cplc(logger, func="Current", value=self.params.get(self.name).get('ccplc-'))

        # Write Pulse: Start
        time.sleep(self.params.get(self.name).get('t_wait'))
        instrument.set_output_value(logger, 'Voltage', val)
        time.sleep(self.params.get(self.name).get('t_write'))
        result_write = instrument.read(logger)
        # Write Pulse: End

        time.sleep(self.params.get(self.name).get('t_wait'))

        # Read Pulse: Start
        instrument.set_output_value(logger, 'Voltage', self.params.get(self.name).get('v_read'))
        time.sleep(self.params.get(self.name).get('t_read'))
        result_read = instrument.read(logger)
        # Read Pulse: End
        
        result = [
            val,     # Voltage Write
            result_write[1],    # Current Write
            result_read[0],     # Voltage Read
            result_read[1],     # Current Read
            result_read[0] / result_read[1],    # Resistance
            result_read[3],     # Timer write
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())    # Timestamp computer
        ]

        match len(self.params.get(self.name).get('cycle')):
            case 1: 
                result_plots = [
                    [[result[0], result[1]],    # [Voltage, Current]    Cycle I-V
                     [result[5], result[4]]],   # [Time, Resistance]    Resistance vs Time
                    [[result[0], result[4]],    # [Voltage, Resistance] Resistance vs Voltage
                     [result[5], result[0]]]    # [Time, Voltage]       Voltage vs Time
                ]

            case 2:
                if val >= 0:
                    result_plots = [
                        [[result[0], result[1]],    # [Voltage, Current]    Cycle I-V +
                         [np.nan, np.nan],          # [NaN, NaN]            Cycle I-V -
                         [result[5], result[4]]],   # [Time, Resistance]    Resistance vs Time
                        [[result[0], result[4]],    # [Voltage, Resistance] Resistance vs Voltage +
                         [np.nan, np.nan],          # [NaN, NaN]            Resistance vs Voltage -
                         [result[5], result[0]]]    # [Time, Voltage]       Voltage vs Time
                    ]
                else:
                    result_plots = [
                        [[np.nan, np.nan],          # [NaN, NaN]            Cycle I-V +
                         [result[0], result[1]],    # [Voltage, Current]    Cycle I-V -
                         [result[5], result[4]]],   # [Time, Resistance]    Resistance vs Time
                        [[np.nan, np.nan],          # [NaN, NaN]            Resistance vs Voltage +
                         [result[0], result[4]],    # [Voltage, Resistance] Resistance vs Voltage -
                         [result[5], result[0]]]    # [Time, Voltage]       Voltage vs Time
                    ]

        return [result, result_plots]

