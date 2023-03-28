from modules.common_utils import *
import pandas as pd

config = load_config()

sample = config.get('sample','name')
device = config.get('sample','device')


folder_path = folder_path(sample,device)
create_path(folder_path)
file = get_filename(folder_path,sample,device)

# save the following section to a 'Input' sheet in the Excel file
sections = ['sourcemeter','measurement','measurement/pulsed']
section_data = dict()
for section in sections:
    section_data.update(dict(config.items(section)))

# Convert the dictionary to a Pandas DataFrame
df = pd.DataFrame(list(section_data.items()), columns=['Key', 'Value'])

# Save the DataFrame to an Excel file
df.to_excel(f'{folder_path}\\{file}', sheet_name='Input', index=False)