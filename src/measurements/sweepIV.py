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
        Initialize the Measurement class.

        Args:
        logger (logging.Logger): Logger to use for logging messages.
        config (dict): Dictionary containing configuration parameters.
        instrument (Instrument): Instrument object to use for measurement.

        """

        self.name = 'sweepIV'
        self.nparams = ['cycle', 'n_cycles', 'v+', 'v-', 'v_step','ccplc+', 'ccplc-', 't_sweep', 'nplc']
        self.headers = ['Voltage [V]', 'Current [A]', 'Resistance [Ω]', 'Timer [s]', 'Datetime']
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
        Set parameters for the plot based on the type of cycle.

        Args:
        cycle_type (str): Type of the cycle which could be '1' or '2'.

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
        Initialize the instrument with initial parameters.

        Args:
        logger (logging.Logger): Logger to use for logging messages.
        instrument (Instrument): Instrument object to use for setting parameters.

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
        logger.debug('Instrument parameters set!')

    def measure_val(self, logger, instrument, val):
        """
        Measure the output for a given voltage and return the result along with the plots.

        Args:
        logger (logging.Logger): Logger to use for logging messages.
        instrument (Instrument): Instrument object to use for measurement.
        val (float): The voltage value to measure.

        Returns:
        list: A list containing the result of measurement and the plots.

        """

        if val>0: instrument.set_func_cplc(logger, func="Current", value=self.params.get(self.name).get('ccplc+'))
        else: instrument.set_func_cplc(logger, func="Current", value=self.params.get(self.name).get('ccplc-'))

        instrument.set_output_value(logger, 'Voltage', val)
        result_sweep = instrument.read(logger)


        time.sleep(self.params.get(self.name).get('t_sweep'))


        
        result = [
            val,                    # Voltage [0]
            result_sweep[1],        # Current [1]
            val /  result_sweep[1], # Resistance [2]
            result_sweep[3],        # Timer [3]
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())    # Datetime [4]
        ]

        match len(self.params.get(self.name).get('cycle')):
            case 1: 
                result_plots = [
                    [[result[0], result[1]],    # [Voltage, Current]    Cycle I-V
                     [result[3], result[2]]],   # [Time, Resistance]    Resistance vs Time   
                    [[result[0], result[2]],    # [Voltage, Resistance] Resistance vs Voltage    
                     [result[3], result[0]]]    # [Time, Voltage]       Voltage vs Time 
                ]

            case 2:
                if val >= 0:
                    result_plots = [
                        [[result[0], result[1]],    # [Voltage, Current]    Cycle I-V +
                         [np.nan, np.nan],          # [NaN, Nan]            Cycle I-V -
                         [result[3], result[2]]],   # [Time, Resistance]    Resistance vs Time
                        [[result[0], result[2]],    # [Voltage, Resistance] Resistance vs Voltage +    
                         [np.nan, np.nan],          # [NaN, NaN]            Resistance vs Voltage -
                         [result[3], result[0]]]    # [Time, Voltage]       Voltage vs Time
                    ]
                else:
                    result_plots = [
                        [[np.nan, np.nan],          # [NaN, NaN]            Cycle I-V +
                         [result[0], result[1]],    # [Voltage, Current]    Cycle I-V -
                         [result[3], result[2]]],   # [Time, Resistance]    Resistance vs Time
                        [[np.nan, np.nan],          # [NaN, NaN]            Resistance vs Voltage +
                         [result[0], result[2]],    # [Voltage, Resistance] Resistance vs Voltage -
                         [result[3], result[0]]]    # [Time, Voltage]       Voltage vs Time
                    ]

        return [result, result_plots]

