import time
import process_memory_stat as proc_mem
from process_cpu_stat import PROCCPU as proc_cpu
from system_cpu_stat import SYSTEMCPU as system_cpu

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
    


def main():

    # environmental variable 
    read_conf("stat.conf")
    timer = int(env_param['duration'])
    pid  = env_param['pid']

    # sensors defn
    proc = proc_cpu(pid)
    sys = system_cpu()
    
    #data container
    process_cpu_info = []
    system_cpu_info = []
    process_mem_info = []
    #get_mem_usage(pid, mem_type='VmSize:', since = 0.0)

    #collect the data from the sensors
    try:
        for i in range (1, timer):
            # read the param
            # sleep for a second
            process_cpu_info.append(proc.get())
            system_cpu_info.append(sys.get())
            process_mem_info.append(proc_mem.get_mem_usage(pid))
            time.sleep(1)
    except KeyboardInterrupt:
        print " \n <Interrupted.Writing to disk>"
    finally:        
        print process_cpu_info
        print system_cpu_info
        print process_mem_info





if __name__ == '__main__':
	main()



