# Imports ----------------------
from rich.console import Console
from rich.traceback import install
from rich.prompt import Prompt
from rich.status import Status
# ------------------------------
from modules.common_utils import *
from modules.measurements import *
from modules.main_handler import MainHandler
# ------------------------------
install()
#Create console
console = Console()

#Verbose debug
verbose = True
logger = verbose_debug(verbose)

#Get config
config = load_config(logger)

MainHandler = MainHandler(console,logger,config)
MainHandler.main()