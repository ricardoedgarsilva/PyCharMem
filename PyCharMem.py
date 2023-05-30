# Imports
import os
import sys
import time
import atexit
import logging
import platform
import importlib
import datetime
import openpyxl
import inquirer
import yaml
import pyvisa
import numpy as np
import pyqtgraph as pg
from openpyxl.drawing.image import Image
from art import text2art
from rich.console import Console
from rich.traceback import install
from rich.logging import RichHandler
from rich.progress import Progress
from rich.panel import Panel
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import (QApplication, QMainWindow, QStyleFactory, QTableWidget,
                              QTableWidgetItem, QVBoxLayout, QWidget, QTabWidget, QGridLayout)

# Global Variables
PROGRAM_INFO = {
    'name': 'PyCharMem',
    'version': '0.0.3',
    'author': 'Ricardo E. Silva',
    'email': 'ricardoedgarsilva@tecnico.ulisboa.pt',
    'description': 'PyCharMem is a Python program that allows you to measure the charge memory of a device.',
    'license': 'GNU General Public License v3.0',
    'url': 'https://github.com/ricardoedgarsilva/PyCharMem'
}


def verbose_debug(verbose: bool) -> logging.Logger:
    log_level = "NOTSET" if verbose else 'INFO'
    logging.basicConfig(level=log_level, format="%(message)s", datefmt="[%X]", handlers=[RichHandler()])
    return logging.getLogger("rich")


def clear_terminal() -> None:
    os.system('cls||clear')


def print_newlines(lines: int) -> None:
    print(lines * "\n")


def splash_screen(console: Console) -> None:
    print(text2art(PROGRAM_INFO['name']))
    console.print(f"Version: {PROGRAM_INFO['version']}", style='bold blue')
    console.print(f"Author: {PROGRAM_INFO['author']}", style='bold blue')
    print_newlines(5)


def open_config(logger: logging.Logger) -> None:
    try:
        os.system({'Windows': 'start config.yml', 'Darwin': 'open config.yml', 'Linux': 'open config.yml'}.get(platform.system(), ''))
    except:
        logger.critical('Config file not found')
        sys.exit()


def read_config(logger: logging.Logger) -> dict:
    try:
        with open('config.yml', 'r') as file:
            config = yaml.safe_load(file)
        logger.info('Config file loaded!')
        return config
    except:
        logger.critical('Config file not found')
        sys.exit()


def path_exists(path: str) -> bool:
    return os.path.exists(path)


def get_path() -> str:
    return os.path.dirname(os.path.realpath(__file__))


def mkdir(logger: logging.Logger, path: str) -> None:
    if not path_exists(path):
        os.makedirs(path)
        logger.debug(f'Folder {path} created')


def get_index(path: str) -> int:
    return len(os.listdir(path))


def get_filename(path: str, sample: str, device: str) -> str:
    index = get_index(path)
    date = datetime.datetime.now().strftime('%Y%m%d')
    return f'{date}_{sample}_{device}_{index}.xlsx'


def get_available_addresses() -> list:
    rm = pyvisa.ResourceManager()
    addresses = rm.list_resources()
    return addresses


def print_available_addresses(logger: logging.Logger, console: Console, addresses: list) -> None:
    print_newlines(1)
    console.print(Panel.fit("[bold]Available Addresses[/bold]", border_style="green"))
    
    if len(addresses) == 0:
        logger.critical('No addresses found!')
    else:
        for address in addresses:
            console.print(address)


def check_address(logger: logging.Logger, addresses: list, address: str) -> None:
    if address not in addresses:
        logger.critical('Instrument address in config file not found! Please edit config file with correct address')
        sys.exit()


def check_missing_params(logger: logging.Logger, my_dict: dict, my_list: list) -> None:
    missing_items = [item for item in my_list if item not in my_dict]

    if len(missing_items) == 0:
        logger.info('All measurement parameters found!')
    else:
        logger.critical('Missing measurement parameters:')
        for item in missing_items:
            logger.critical(f'- {item}')
        sys.exit()


def create_list(logger: logging.Logger, condition_values: list) -> np.ndarray:
    cycle, max_value, min_value, step = condition_values
    listp_oneway = np.arange(0, max_value, step)
    listn_oneway = np.arange(0, min_value, -step)
    listp = np.concatenate((listp_oneway, np.array([max_value]), np.flip(listp_oneway)))
    listn = np.concatenate((listn_oneway, np.array([min_value]), np.flip(listn_oneway)))

    try:
        cycle_dict = {'+': listp, '-': listn, '+-': np.concatenate((listp, listn)), '-+': np.concatenate((listn, listp))}
        return cycle_dict[cycle]
    except KeyError:
        logger.critical('Invalid cycle type!')
        sys.exit()


def get_datetime() -> str:
    return datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S:%f')

def import_module(logger: logging.Logger, type: str, inst_type=None, measurement_type=None) -> type:
    file_name, obj_name = '', ''
    
    if type == 'instrument':
        file_name = f'instruments.{inst_type}'
        obj_name = 'Instrument'
    elif type == 'measurement':
        file_name = f'measurements.{measurement_type}'
        obj_name = 'Measurement'
    else:
        logger.critical('Invalid type passed to import_module!')
        sys.exit()

    file = importlib.import_module(file_name)
    logger.debug(f'{file_name} module imported')
    obj = getattr(file, obj_name)
    logger.debug(f'{obj_name} class imported')
    return obj

def menu(logger: logging.Logger, console: Console, type: str) -> str:
    name, message, choices = '', '', []
    
    if type == 'main':
        name = 'Main Menu'
        message = 'Select an option:'
        choices = ['Exit', 'Select Measurement', 'Print Available Addresses', 'Edit Configuration']
    elif type == 'measurements':
        try:
            list_dir = os.listdir('measurements')
            measurement_types = [filename.split('.')[0] for filename in list_dir if filename.endswith('.py')]
            logger.debug(f'{len(measurement_types)} measurement types found')
        except:
            logger.critical('No measurement types found!')
            sys.exit()
        
        name = 'Measurement Selection Menu'
        message = 'Select a measurement:'
        choices = measurement_types
        choices.append('Back')
    else:
        logger.critical('Invalid menu type passed to menu function!')
        sys.exit()

    print_newlines(1)
    console.print(Panel.fit(f"[bold]{name}[/bold]", border_style="green"))
    menu_options = [inquirer.List('choice', message=message, choices=choices)]
    answer = inquirer.prompt(menu_options)
    logger.debug(f'Returning answer: {answer}')
    return answer['choice']

def ask_for_comment(logger: logging.Logger) -> str:
    print_newlines(2)
    comment = [inquirer.Text('comment', message="What would you like to comment?", validate=lambda _, x: len(x) > 0),]
    answer = inquirer.prompt(comment)
    logger.debug(f'Comment: {answer}')
    return answer['comment']

def repeat_measurement(logger: logging.Logger, console: Console) -> bool:
    print_newlines(2)
    comment = [inquirer.Confirm('repeat', message="Would you like to repeat the measurement?")]
    answer = inquirer.prompt(comment)
    logger.debug(f'Repeat: {answer}')
    return answer['repeat']

def exit(logger: logging.Logger, inst: object) -> None:
        logger.info('Exiting program...') 
        inst.close(logger)
        logger.info('Instrument closed')
        time.sleep(2)


# Important Classes

class FileSave:
    def __init__(self, logger: logging.Logger, sample: str, device: str):
        self.path = os.path.join(get_path(), "data", sample, device)
        mkdir(logger, self.path)

        self.file_name = get_filename(self.path, sample, device)
        self.file_path = os.path.join(self.path, self.file_name)
        self.wb = openpyxl.Workbook()
        self.wb.create_sheet('config')
        self.wb.create_sheet('data')
        self.wb.remove(self.wb['Sheet'])
        self.wb.save(self.file_path)

    def save_config(self, logger: logging.Logger, config: dict, measurement_type: str):
        self.ws = self.wb['config']

        sections = ['sample', 'instrument', measurement_type]
        for section in sections:
            self.ws.append([section])
            for key, value in config.get(section).items():
                self.ws.append([key, value])
            self.ws.append([])
        self.wb.save(self.file_path)
        logger.debug('Configuration file saved in config sheet')

    def save_headers(self, logger: logging.Logger, headers_list: list):
        self.ws = self.wb['data']
        for i in range(len(headers_list)):
            self.ws.cell(row=1, column=i + 1).value = headers_list[i]
        self.wb.save(self.file_path)
        logger.debug('Headers saved in data sheet')

    def save_result(self, logger: logging.Logger, result: list):
        self.ws = self.wb['data']
        row = self.ws.max_row + 1
        for i in range(len(result)):
            self.ws.cell(row=row, column=i + 1).value = result[i]
        self.wb.save(self.file_path)
        logger.debug('result saved in data sheet')



class Logbook:
    def __init__(self, logger: logging.Logger, sample: str):
        self.path = os.path.join(get_path(), "data", sample)
        mkdir(logger, self.path)

        self.file_path = os.path.join(self.path, 'logbook.xlsx')

        if path_exists(self.file_path):
            self.wb = openpyxl.load_workbook(self.file_path)
            logger.debug('Logbook file already exists')
        else:
            self.wb = openpyxl.Workbook()
            self.wb.create_sheet('logbook')
            self.wb.remove(self.wb['Sheet'])

            self.ws = self.wb['logbook']
            self.ws.title = 'logbook'
            headers_list = ['Date', 'File', 'Comment']
            for i in range(len(headers_list)):
                self.ws.cell(row=1, column=i + 1).value = headers_list[i]

            self.wb.save(self.file_path)
            logger.debug('Logbook file created')

    def save_log(self, logger: logging.Logger, date: str, file: str, comment: str):
        self.ws = self.wb['logbook']
        row = self.ws.max_row + 1
        self.ws.cell(row=row, column=1).value = date
        self.ws.cell(row=row, column=2).value = file
        self.ws.cell(row=row, column=3).value = comment
        self.wb.save(self.file_path)
        logger.debug('Log saved in logbook sheet')


class MeasurementThread(QThread):
    update_data = pyqtSignal(object, list)
    clear_plots = pyqtSignal(list, list)
    close_window = pyqtSignal()

    def __init__(self, logger, inst, meas, config):
        super().__init__()
        self.logger = logger
        self.inst = inst
        self.meas = meas
        self.config = config
        self.filesave = FileSave(logger, config.get('sample').get('name'), config.get('sample').get('device'))
        self.filesave.save_config(logger, config, meas.name)
        self.filesave.save_headers(logger, self.meas.headers)
        self.n_cycles = config.get(meas.name).get('n_cycles')
        self.n_vals = len(self.meas.vals)

    def run(self):
        self.inst.set_output_state(self.logger,'ON')
        self.inst.write(self.logger, 'INIT:IMM')
        

        with Progress() as progress:
            value_task = progress.add_task(f"[purple] Current value: None", total=self.n_vals) 
            cycle_task = progress.add_task(f"[blue]Cycle 0/{self.n_cycles}", total=self.n_cycles)
            for cycle in range(1, self.n_cycles + 1):
                for val in self.meas.vals:
                    results = self.meas.measure_val(self.logger, self.inst, val)
                    self.filesave.save_result(self.logger, results[0])
                    self.update_data.emit(self.meas, results)
                    progress.update(value_task, advance=1, description=f"[purple]Current value: {val}")
                self.clear_plots.emit(self.meas.plot_grid,self.meas.plot_clear)
                progress.update(value_task, advance=-self.n_vals, description=f"[purple]Value 0/{self.n_vals}")
                progress.update(cycle_task, advance=1, description=f"[blue]Cycle {cycle}/{self.n_cycles}")
            self.inst.set_output_state(self.logger,'OFF')

        
        logbook = Logbook(self.logger, self.config.get('sample').get('name'))
        self.logger.info('Measurement finished! Please enter a comment for the logbook')
        comment = ask_for_comment(self.logger)
        logbook.save_log(self.logger, get_datetime(), self.filesave.file_name, comment)
        self.close_window.emit()
        self.logger.info('Logbook saved!')


class MeasurementWindow(QMainWindow):
    def __init__(self, logger, inst, meas, config):
        super().__init__()
        self.initUI(meas)
        self.measure = MeasurementThread(logger, inst, meas, config)
        self.measure.update_data.connect(self.update_data)
        self.measure.clear_plots.connect(self.clear_plots)
        self.measure.close_window.connect(self.close)
        self.measure.start()

    def initUI(self, meas):
        self.setWindowTitle(meas.name)
        self.setGeometry(100, 100, 800, 600)

        self.tab_widget = QTabWidget(self)
        plot_tab = QWidget()
        plot_layout = QVBoxLayout(plot_tab)
        self.plot_grid = QGridLayout()
        [rows, cols] = meas.plot_grid
        self.data_plots = [[[] for _ in range(cols)] for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                plot_widget = pg.PlotWidget()
                plot_widget.setTitle(meas.plot_titles[row][col])
                plot_widget.showGrid(x=True, y=True)
                plot_widget.setLabel('bottom', meas.plot_labels[row][col][0])
                plot_widget.setLabel('left', meas.plot_labels[row][col][1])
                self.plot_grid.addWidget(plot_widget, row, col)

        plot_layout.addLayout(self.plot_grid)
        plot_tab.setLayout(plot_layout)
        self.tab_widget.addTab(plot_tab, "Plots")

        data_tab = QWidget()
        data_layout = QVBoxLayout(data_tab)
        self.data_table = QTableWidget()
        self.data_table.setRowCount(0)
        self.data_table.setColumnCount(len(meas.headers))
        self.data_table.setHorizontalHeaderLabels(meas.headers)
        data_layout.addWidget(self.data_table)
        data_tab.setLayout(data_layout)
        self.tab_widget.addTab(data_tab, "Data")

        self.setCentralWidget(self.tab_widget)

    def update_data(self, meas, results):
        [result, result_plots] = results
        self.data_table.insertRow(0)
        for col in range(len(meas.headers)):
            item = QTableWidgetItem(str(result[col]))
            self.data_table.setItem(0, col, item)

        for row in range(meas.plot_grid[0]):
            for col in range(meas.plot_grid[1]):
                self.data_plots[row][col].append(result_plots[row][col])
                plot_widget = self.plot_grid.itemAtPosition(row, col).widget()
                plot_widget.plot(
                    np.array(self.data_plots[row][col])[:,0],
                    np.array(self.data_plots[row][col])[:,1], 
                    clear=True)
        
    def clear_plots(self, plot_grid, plot_clear):
    
        for row in range(plot_grid[0]):
            for col in range(plot_grid[1]):
                if plot_clear[row][col]:
                    self.data_plots[row][col] = []

    def close_window(self):
        self.close()


# Main Functions ------------------------------------------------------------------

def start_gui(logger: logging.Logger, inst: object, meas: object, config: dict):
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))
    app.setStyleSheet("QMainWindow::title {background-color: #333333;}")
    window = MeasurementWindow(logger, inst, meas, config)
    window.show()
    app.exec()


def main():
    install()
    console = Console()
    logger = verbose_debug(False)
    running = True

    clear_terminal()
    splash_screen(console)

    config = read_config(logger)

    addresses = get_available_addresses()
    print_available_addresses(logger, console, addresses)

    inst_class = import_module(logger=logger, type='instrument', inst_type=config.get('instrument').get('model'))
    inst = inst_class(logger, config)
    inst.reset(logger)
    logger.info('Instrument loaded')
    atexit.register(exit, logger, inst)

    while running:
        option = menu(logger, console, 'main')
        

        match option:
            case 'Exit':
                running = False

            case 'Print Available Addresses':
                print_available_addresses(logger, console, get_available_addresses())

            case 'Edit Configuration':
                open_config(logger)

            case 'Select Measurement':
                config = read_config(logger)
                option2 = menu(logger, console, 'measurements')
                if option2 == 'Back': continue

                meas_class = import_module(logger=logger, type='measurement', measurement_type=option2)
                meas = meas_class(logger, config, inst)

                check_missing_params(logger, meas.params[meas.name], meas.nparams)
                logger.info('All parameters present')
                start_gui(logger, inst, meas, config)
                option3 = repeat_measurement(logger, console)
                if option3: continue
                else: 
                    running = False




if __name__ == "__main__":
    main()



