# Measurement class for sweeping voltages and measuring voltage
import time
import numpy as np


def create_list(logger, cycle, max_val, min_val, step):
    list_positive = np.concatenate((np.arange(0, max_val, step), [max_val], np.flip(np.arange(0, max_val, step))))
    list_negative = np.concatenate((np.arange(0, min_val, -step), [min_val], np.flip(np.arange(0, min_val, -step))))

    try:
        match cycle:
            case '+': return list_positive
            case '-': return list_negative
            case '+-': return np.concatenate((list_positive, list_negative))
            case '-+': return np.concatenate((list_negative, list_positive))
    except:
        logger.critical('Invalid cycle type!')
        quit()


class Measurement:
    def __init__(self, logger, config, instrument) -> None:
        self.name = 'pulsedVI'
        self.nparams = ['cycle', 'n_cycles', 'i+', 'i-', 'i_step', 'i_read', 'vcplc+','vcplc-', 't_write', 't_read', 't_wait', 'nplc']

        self.headers = ['Current Write[A]', 'Voltage Write [A]', 'Current Read [V]', 'Voltage Read [A]', 'Resistance [Ω]', 'Timer [s]', 'Datetime']

        self.params = dict(config.items())
        self.vals = create_list(
            logger,
            self.params.get(self.name).get('cycle'),
            self.params.get(self.name).get('i+'),
            self.params.get(self.name).get('i-'),
            self.params.get(self.name).get('i_step')
        )

        self.set_plot_parameters(self.params.get(self.name).get('cycle'))
        self.initialize_instrument(logger, instrument)

    def set_plot_parameters(self, cycle_type):
        match len(cycle_type):
                case 1: 
                    self.plot_grid = (2, 2)
                    self.plot_titles = [[f'Cycle V-I  {cycle_type}', 'Resistance vs Time'],
                                        ['Resistance vs Voltage', 'Current vs Time']]
                    self.plot_labels = [
                        [['Current [A]','Voltage [V]'],
                        ['Time [s]', 'Resistance [Ω]']],
                        [['Current [A]', 'Resistance [Ω]'],
                        ['Time [s]', 'Current [A]']]]
                    self.plot_clear = [[True, False], [True, False]]
                case 2:
                    self.plot_grid = (2, 3)
                    self.plot_titles = [['Cycle V-I +', 'Cycle V-I -', 'Resistance vs Time'],
                                        ['Resistance vs Current +', 'Resistance vs Current -', 'Current vs Time']]
                    self.plot_labels = [
                        [['Current [A]','Voltage [V]'], [ 'Current [A]', 'Voltage [V]'], ['Time [s]', 'Resistance [Ω]']],
                        [['Current [A]', 'Resistance [Ω]'], ['Current[A]', 'Resistance [Ω]'], ['Time [s]', 'Current [A]']]]
                    self.plot_clear = [[True, True, False], [True, True, False]]

    def initialize_instrument(self, logger, instrument):
        logger.debug('Setting instrument initial parameters')
        instrument.reset(logger)
        instrument.set_mode_fixed(logger, func="Current")
        instrument.set_src_func(logger, func="Current")
        instrument.set_sense_func(logger, func="Current")
        instrument.set_func_range(logger, func="Current")
        instrument.set_func_nplc(logger, func="Current", value=self.params.get(self.name).get('nplc'))
        instrument.set_sense_func(logger, func="Voltage")
        instrument.set_func_range(logger, func="Voltage")
        logger.debug('Instrument parameters set!')

    def measure_val(self, logger, instrument, val):
        if val>0: instrument.set_func_cplc(logger, func="Voltage", value=self.params.get(self.name).get('vcplc+'))
        else: instrument.set_func_cplc(logger, func="Voltage", value=self.params.get(self.name).get('vcplc-'))

        time.sleep(self.params.get(self.name).get('t_wait'))


        #Write Pulse: Start
        instrument.set_output_value(logger, "Current", val)
        time.sleep(self.params.get(self.name).get('t_write'))
        result_write = instrument.read(logger)
        #Write Pulse: End

        instrument.set_output_value(logger, "Current", 0)
        time.sleep(self.params.get(self.name).get('t_wait'))

        #Read Pulse: Start
        instrument.set_output_value(logger, "Current", self.params.get(self.name).get('i_read'))
        time.sleep(self.params.get(self.name).get('t_read'))
        result_read = instrument.read(logger)
        #Read Pulse: End

        result = [
            result_write[1], #Current Write
            result_write[0], #Voltage Write
            result_read[1], #Current Read
            result_read[0], #Voltage Read
            result_read[0]/result_read[1], #Resistance
            result_read[3], #Timer
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) #Datetime
        ]


        match len(self.params.get(self.name).get('cycle')):
            case 1: 
                result_plots = [
                    [[result[0], result[1]],  # Cycle V-I
                     [result[5], result[4]]],  # Resistance vs Time
                    [[result[0], result[4]],  # Resistance vs Current
                     [result[5], result[0]]]   # Current vs Time
                ]
            case 2:
                if val >= 0:
                    result_plots = [
                        [[result[0], result[1]],  # Cycle V-I +
                         [np.nan, np.nan],
                         [result[5], result[4]]],  # Resistance vs Time
                        [[result[0], result[4]],  # Resistance vs Voltage +
                         [np.nan, np.nan],
                         [result[5], result[0]]]   # Voltage vs Time
                    ]
                else:
                    result_plots = [
                        [[np.nan, np.nan],
                         [result[0], result[1]],  # Cycle V-I -
                         [result[5], result[4]]],  # Resistance vs Time
                        [[np.nan, np.nan],
                         [result[0], result[4]],  # Resistance vs Voltage -
                         [result[5], result[0]]]   # Current vs Time
                    ]

        return [result, result_plots]                


        