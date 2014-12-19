import time
from process_cpu_stat import PROCCPU as process
from system_cpu_stat import SYSTEMCPU as system

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
    proc = process(pid)
    sys = system()
    
    #data container
    process_cpu_info = []
    system_cpu_info = []


    #collect the data from the sensors
    try:
        for i in range (1, timer):
            # read the param
            # sleep for a second
            process_cpu_info.append(proc.get())
            system_cpu_info.append(sys.get())
            time.sleep(1)
    except KeyboardInterrupt:
        print " \n <Interrupted.Writing to disk>"
    finally:        
        print process_cpu_info
        print system_cpu_info





if __name__ == '__main__':
	main()



