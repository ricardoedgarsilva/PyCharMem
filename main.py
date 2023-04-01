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
logger = verbose_debug(False)

#Get config
config = config_load(logger)
MainHandler = MainHandler(logger,console,config)
MainHandler.main()