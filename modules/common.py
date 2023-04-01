











def check_missing_params(logger,my_dict, my_list):
    '''Checks if the dictionary has all the keys in the list'''
    
    missing_items = [item for item in my_list if item not in my_dict]

    if len(missing_items) == 0:
        logger.info('All parameters found!')
    else:
        logger.critical('Missing parameters:')
        for item in missing_items:
            logger.critical(f'- {item}')
        quit()

def create_list(logger,cycle,max,min,step):
    '''Creates a list of values'''
    import numpy as np

    list1 = np.arange(0,max,step)
    listp = np.concatenate((list1,np.array([max]),np.flip(list1)))

    list2 = np.arange(0,min,-step)
    listn = np.concatenate((list2,np.array([min]),np.flip(list2)))

    try:
        match cycle:
            case '+': return listp
            case '-': return listn
            case '+-': return np.concatenate((listp,listn))
            case '-+': return np.concatenate((listn,listp))
    except:
        logger.critical('Invalid cycle type!')
        quit()
    
def timestamp():
    '''Returns timestamp'''
    import datetime
    import time
    return datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S:%f')

def import_module(logger,type,srcmtr_model=None,measurement_type=None,plot_type=None):
    '''Imports a module from string'''
    import importlib
    logger.debug(f'Importing {type} module')
    try:
        match type:
            case 'sourcemeter':
                file_name = f'sourcemeters.{srcmtr_model}'
                obj_name = 'Sourcemeter'
            
            case 'measurement':
                file_name = f'measurements.{measurement_type}'
                obj_name = 'Measurement'

            
            case 'plot':
                file_name = f'plots.{plot_type}'
                obj_name = 'Plots'

        file = importlib.import_module(file_name)
        logger.debug(f'{file_name} module imported')
        obj = getattr(file, obj_name)
        logger.debug(f'{obj_name} class imported')
        return obj
    
    except:
        logger.critical(f'{type} could not be imported!')
        quit()