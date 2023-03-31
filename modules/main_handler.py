#Creates main handler object
from modules.common import *
from modules.interface import menu
from rich.progress import Progress
import numpy as np


class MainHandler:
    def __init__(self,logger,console,config):
        #Create object variables
        self.running = True
        self.logger = logger
        self.console = console
        self.config = config
        self.data = np.array([])
        #Splash screen
        clear_terminal()
        splash_screen(console)

        #Open Sourcemeter
        scrmtr_model = config.get('sourcemeter','model')
        sourcemeter_class = import_module(logger=self.logger,type='sourcemeter',srcmtr_model=scrmtr_model)
        self.sourcemeter = sourcemeter_class(self.logger,self.config)


        #Sucefully loaded
        self.logger.info('Loading complete!')
        print_available_addresses(self.console,self.logger)


    def main(self):
        while self.running:
            self.main_option = menu(self.logger,self.console,'main')
    
            match self.main_option:
                case 'Exit': self.running = False
                case 'Print Available Addresses': print_available_addresses(self.logger,self.console)
                case 'Edit Configuration': config_edit(self.logger)
                case 'Select Measurement':
                    #Reload config file in case of changes and select measurement
                    self.config = config_load(self.logger)
                    self.meas_type = menu(self.logger,self.console,'measurements')

                    #Return to main menu
                    if self.meas_type == 'Back': continue
                    
                    #Import measurement file
                    measurement_type = import_module(self.logger,self.meas_type,self.config)
                    module = importlib.import_module(f'measurements.{self.meas_type}')
                    measurement_type = getattr(module, 'Measurement')
                    measurement = measurement_type(self.config, self.console, self.logger)
                    measurement.set_sourcemeter(self.sourcemeter)

                    try:
                        #
                        module = importlib.import_module(f'plots.{self.plot_name}')
                        plot_type = getattr(module, 'Plot')
                        self.plots = plot_type()
                        self.logger.info(f'Loaded plot: {self.plot_name}')
                    except:
                        self.logger.critical(f'Could not load plot: {self.plot_name}')
                        quit()

                    n_cycles = measurement.n_cycle
                    #save_config(self.config,self.logger)

                    with Progress() as progress:
                        task = progress.add_task("[green]Measuring", total=n_cycles)

                        for i in range(n_cycles):
                            progress.update(task, advance=1, description=f"[blue]Cycle {i}/{n_cycles}")
                            #measurement.measure_cycle(self.sourcemeter)
                            self.data = np.concatenate((self.data, measurement.result))

                            self.plots.add_result(measurement.result)
                            self.plots.update()
                            

                    measurement.measure_cycle(self.sourcemeter)
                    self.data.concat(measurement.result)


                


