#Creates main handler object
from modules.common import *
from modules.filesaver import FileSaver
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
        self.data = []
        #Splash screen
        clear_terminal()
        splash_screen(console)

        #Print available addresses
        print_available_addresses(self.logger,self.console)

        
        #Load sourcemeter
        sourcemeter_class = import_module(logger=self.logger,type='sourcemeter',srcmtr_model=config.get('sourcemeter','model'))
        self.sourcemeter = sourcemeter_class(self.logger,self.config)


        #Sucefully loaded
        self.logger.info('Loading complete!')

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

                    #Import filesaver
                    self.filesaver = FileSaver(self.logger,self.config.get('sample','name'),self.config.get('sample','device'))
                    
                    #Import measurement file
                    measurement_class = import_module(logger=self.logger, type='measurement',measurement_type=self.meas_type)
                    measurement = measurement_class(self.logger,self.config,self.filesaver)
                    measurement.set_sourcemeter(self.logger,self.sourcemeter)



                    try:
                        #
                        self.plot_class = import_module(logger=self.logger,type='plot',plot_type=measurement.plot_name)
                        self.plots = self.plot_class()
                        self.logger.info(f'Loaded plot: {measurement.plot_name}')
                    except:
                        self.logger.critical(f'Could not load plot: {measurement.plot_name}')
                        quit()

                    n_cycles = measurement.n_cycle

                    # IMPLEMENT MEASUREMENT CYCLE
                    #save_config(self.config,self.logger)

                    with Progress() as progress:
                        task = progress.add_task("[green]Measuring", total=n_cycles)

                        for i in range(n_cycles):
                            measurement.measure_cycle(self.logger,self.sourcemeter,self.plots)
                            self.data.append((self.data, measurement.result))
                            progress.update(task, advance=1, description=f"[blue]Cycle {i}/{n_cycles}")
                        
                        self.plots.show()
                            

                    self.logger.info(f'Finished measurement: {measurement.name}')




                


