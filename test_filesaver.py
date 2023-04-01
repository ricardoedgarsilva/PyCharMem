import os
from rich.console import Console
from rich.traceback import install
from rich.prompt import Prompt
from rich.status import Status
from configparser import ConfigParser
# ------------------------------
from modules.common import *
from modules.main_handler import MainHandler

from openpyxl.drawing.image import Image
# ------------------------------

install()           #Rich traceback
console = Console() #Rich console
logger = verbose_debug(False)

config = ConfigParser()
config.read('config.ini')


sample = config.get('sample','name')
device = config.get('sample','device')



filesaver = FileSaver(sample,device,logger)
filesaver.save_config(config,'pulsedVI')

headers = ['time','voltage','current']
filesaver.save_headers(headers)

return_value = [1,2,3]

for i in range(10):
    filesaver.save_result(return_value)

filesaver.save_plots(Image('test_plot.png'))