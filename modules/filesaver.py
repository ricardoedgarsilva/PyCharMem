import os
import pandas as pd
from modules.common import path_exists, get_path, mkdir, get_filename

class FileSaver:
    def __init__(self, sample, device,logger):
        self.path = os.path.join(get_path(), "data", sample, device)
        mkdir(self.path,logger)
        self.file_name = get_filename(self.path,sample,device)
        self.file_path = os.path.join(self.path, self.file_name)

        
    def save_config(self, config, logger):
        df = pd.DataFrame.from_dict(config._sections)
        df = df.transpose()
        print(df)
        writer = pd.ExcelWriter(self.file_path, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='config', index=False)
        writer.save()
        logger.info('Config file saved!')
    
    def save_headers(self, headers_list, logger):
        df = pd.DataFrame(headers_list, columns=["Header"])
        df.to_excel(self.file_path,sheet_name='data')
        logger.info('Headers saved!')
