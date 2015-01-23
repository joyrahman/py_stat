import process_memory_stat as proc_mem
from process_cpu_stat import PROCCPU as proc_cpu
from system_cpu_stat import SYSTEMCPU as system_cpu
import sys
import write_to_csv as csv
import time
import proc_to_pid
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


def get_stat(pid, proc_name, timer = 120 ):
    main(pid, proc_name, timer)

def main_sys_arg():
    proc_name = "zerovm"
    timer = 240
    pids = proc_to_pid.get_pid(proc_name)
    main(pids[0], proc_name, timer)
    
def main(pid="", proc_name="", timer=""):

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
            current_time = time.clock() 
            # csv format: time, user_cpu, kernel_cpu, sys_cpu, proc_mem, sys_mem
            csv_data.append([current_time,process_cpu_reading_user, \
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
        #write_to_csv(csv_data)
        #return csv_data
        csv.write_to_csv(pid,proc_name,csv_data)





if __name__ == '__main__':
	main_sys_arg()



