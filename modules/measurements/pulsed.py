def measure_pulsed(sourcemeter,config):

    #Read configuration file
    cycle   =   config.getint('measurement','cycle')
    t_write =   config.getfloat('measurement/pulsed','t_write')
    t_read  =   config.getfloat('measurement/pulsed','t_read')
    t_wait  =   config.getfloat('measurement/pulsed','t_wait')
    n_cycle =   config.getint('measurement/pulsed','n_cycle')
    v_read  =   config.getfloat('measurement/pulsed','v_read')
    v_step  =   config.getfloat('measurement/pulsed','v_step')
    v_max   =   config.getfloat('measurement/pulsed','v_max')
    v_min   =   config.getfloat('measurement/pulsed','v_min')   

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