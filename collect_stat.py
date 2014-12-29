import time
import process_memory_stat as proc_mem
from process_cpu_stat import PROCCPU as proc_cpu
from system_cpu_stat import SYSTEMCPU as system_cpu
import csv
import sys
# stores parameter set from config file
env_param = {}


def read_conf(config_file):
    with open(config_file) as fp:
        for line in fp:
            (key,val) = line.strip().split("=")
            env_param[str.strip(key)] = str.strip(val)
            
def print_dict(dict_param=env_param):
    for key in dict_param.keys():
        print key,"=",dict_param[key]
    
def write_to_csv(pid="",csv_data):
    #pass
    print csv_data
    #file name format : procname_pid_time.csv

    output_file_name = get_process_name(pid)+\
            "_"+pid+"_"+str(time.time())+".csv" 
    
    with open(output_file_name,'w',newline='') as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerows(csv_data)


def get_process_name(pid):
    return "dummy"

def get_stat(pid,timer = 120 ):
    main(pid,timer)


def main(pid="", timer=""):

    #set  environmental variable if param are not defined 
    read_conf("stat.conf")
    if not pid:
        pid  = env_param['pid']
    if not timer:
        timer = int(env_param['duration'])
    
    # sensors defn
    proc = proc_cpu(pid)
    sys = system_cpu()
    
    #data container
    csv_data = []
    #get_mem_usage(pid, mem_type='VmSize:', since = 0.0)

    #collect the data from the sensors
    try:
        for i in range (0, timer):
            process_cpu_reading_user,process_cpu_reading_karnel =  proc.get()
            system_cpu_reading  =  sys.get()
            process_memory_reading = proc_mem.get_mem_usage(pid)
            system_memory_reading =  proc_mem.get_system_mem_size()
            csv_data.append([process_cpu_reading_user, \
                    process_cpu_reading_karnel, \
                    system_cpu_reading, \
                    process_memory_reading,\
                    system_memory_reading])
            time.sleep(1)
    except KeyboardInterrupt:
        print " \n <Interrupted.Writing to disk>"
    
    except Exception as Inst:
        print ":("
        print Inst
    
    finally:        
        write_to_csv(csv_data)

        





if __name__ == '__main__':
	main()



