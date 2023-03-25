






def save():
    pass


def measurement_pulsed():

    #Read configuration file
    cycle   =   config.getint('measurementVI','cycle')
    t_write =   config.getfloat('measurementVI/pulsed','t_write')
    t_read  =   config.getfloat('measurementVI/pulsed','t_read')
    t_wait  =   config.getfloat('measurementVI/pulsed','t_wait')
    n_cycle =   config.getint('measurementVI/pulsed','n_cycle')
    v_read  =   config.getfloat('measurementVI/pulsed','v_read')
    v_step  =   config.getfloat('measurementVI/pulsed','v_step')
    v_max   =   config.getfloat('measurementVI/pulsed','v_max')
    v_min   =   config.getfloat('measurementVI/pulsed','v_min')


    #Create voltage lists for each cycle
    vlistp  =   np.concatenate((np.arange(0, v_max+v_step, v_step), np.arange(v_max-v_step, -v_step, -v_step)))
    vlistn  =   np.concatenate((np.arange(0, v_min-v_step, -v_step), np.arange(v_min+v_step, v_step, v_step)))
    
    match cycle:
        case '+':   voltage_list = vlistp
        case '-':   voltage_list = vlistn
        case '+-':  voltage_list = np.concatenate(vlistp,vlistn)
        case '-+':  voltage_list = np.concatenate(vlistn,vlistp)


    for cycle_i in range(n_cycle):
        for voltage_val in voltage_list:
            #write pulse
            sourcemeter.write('SOUR:VOLT {}'.format(voltage_val))
            sourcemeter.write('OUTP ON')
            time.sleep(t_write)
            current_write = sourcemeter.query('MEAS:CURR?')
            sourcemeter.write('OUTP OFF')

            #wait some time
            time.sleep(t_wait)
            
            #read pulse
            sourcemeter.write('SOUR:VOLT {}'.format(v_read))
            sourcemeter.write('OUTP ON')
            time.sleep(t_read)
            current_read = sourcemeter.query('MEAS:CURR?')
            sourcemeter.write('OUTP OFF')

            







sourcemeter.close()
