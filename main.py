# Imports ----------------------
from rich.console import Console
from rich.traceback import install
from rich.prompt import Prompt
from rich.status import Status
# ------------------------------
from modules.common import *
from modules.main_handler import MainHandler
# ------------------------------

install()           #Rich traceback
console = Console() #Rich console
logger = verbose_debug(True)

#Get config
config = load_config(logger)

MainHandler = MainHandler(console,logger,config)
MainHandler.main()