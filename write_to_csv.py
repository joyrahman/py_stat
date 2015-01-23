import csv
import datetime
import time
import os
import logging
def write_to_csv(pid, process_name, csv_data):
    #pass
    #print csv_data
    #file name format : procname_pid_time.csv
    process_name = "zerovm"
    time_format = '%Y%m%d_%H%M%S'
    current_time = time.strftime(time_format)
    file_extension = "csv"
    directory_name = "csv_report"
    if not os.path.exists(directory_name):
        os.makedir(directory_name)
    output_file_name = "{}_{}_{}.{}".format( process_name,\
            pid, current_time,\
            file_extension) 
    '''
    output_file_name = process_name +\
            "_" + pid + "_" + \
            current_time.strftime(time_format)\
            + ".csv" 
    '''        
    #print "csv output to: " + output_file_name    
    logging.debug("csv output to: {}".format(output_file_name))
    with open(directory_name + "/" + output_file_name,'w') as fp: 
        a = csv.writer(fp, delimiter=',')
        a.writerows(csv_data)


