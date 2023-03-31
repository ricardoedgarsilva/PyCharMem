import os
from rich.console import Console
from rich.traceback import install
from rich.prompt import Prompt
from rich.status import Status
from configparser import ConfigParser
# ------------------------------
from modules.common import *
from modules.main_handler import MainHandler
import openpyxl
from openpyxl.drawing.image import Image
# ------------------------------

install()           #Rich traceback
console = Console() #Rich console
logger = verbose_debug(False)

config = ConfigParser()
config.read('config.ini')


sample = config.get('sample','name')
device = config.get('sample','device')


class FileSaver:
    def __init__(self, sample, device,logger):
        self.path = os.path.join(get_path(), "data", sample, device)
        self.logbook_path = os.path.join(get_path(), "data", sample,'logbook.xlsx')
        mkdir(self.path,logger)
        self.file_name = get_filename(self.path,sample,device)
        self.file_path = os.path.join(self.path, self.file_name)

        #debug
        logger.debug(f'Data file path: {self.file_path}')
        logger.debug(f'Logbook file path: {self.logbook_path}')

        #create excel file
        self.wb = openpyxl.Workbook()
        self.wb.create_sheet('config')
        self.wb.create_sheet('data')
        self.wb.create_sheet('plots')
        self.wb.remove(self.wb['Sheet'])
        self.wb.save(self.file_path)

        #create logbook
        self.logbook = openpyxl.Workbook()
        try:
            self.logbook = openpyxl.load_workbook(self.logbook_path)
            logger.debug('Logbook loaded')
        except:
            self.logbook.create_sheet('logbook')
            self.logbook.remove(self.logbook['Sheet'])
            self.logbook.save(self.logbook_path)
            logger.debug('Logbook created')
        
    def save_config(self,config,measurement_type,logger):
        #create excel sheet
        self.ws = self.wb['config']
        self.ws.title = 'config'

        #read config file
        sections = ['sample','sourcemeter',f'measurement/{measurement_type}']
        for section in sections:
            self.ws.append([section])
            for key, value in config.items(section):
                self.ws.append([key,value])
            self.ws.append([])
        self.wb.save(self.file_path)
        logger.debug('Config sheet saved')

    def save_headers(self, headers_list):
        self.ws = self.wb['data']
        self.ws.title = 'data'
        for i in range(len(headers_list)):
            self.ws.cell(row=1, column=i+1).value = headers_list[i]
        self.wb.save(self.file_path)

    def save_result(self,result):
        self.ws = self.wb['data']
        row = self.ws.max_row + 1
        for i in range(len(result)):
            self.ws.cell(row=row, column=i+1).value = result[i]
        self.wb.save(self.file_path)
    
    def save_plots(self,image):
        self.ws = self.wb['plots']
        self.ws.add_image(image, 'B1')
        self.wb.save(self.file_path)


filesaver = FileSaver(sample,device,logger)
filesaver.save_config(config,'pulsedVI')

headers = ['time','voltage','current']
filesaver.save_headers(headers)

return_value = [1,2,3]

for i in range(10):
    filesaver.save_result(return_value)

filesaver.save_plots(Image('test_plot.png'))