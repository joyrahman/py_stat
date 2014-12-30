import os
import sys
import logger


pids = []
process = {}

def usage():
    print 'python get_pid.py <process_name>'
    sys.exit(1)


def print_dict():
    global pids
    global process
    for key in process:
        print key,"=>",process[key]


def add_to_dict(x):
    global pids 
    global process
    pid_start_position = 9
    pid_end_position = 15
    proc_name_start_position = 49
    proc_name_end_position = 60

    pids.append(int(x[pid_start_position:pid_end_position]))
    process[int(x[pid_start_position:pid_end_position])] = x[proc_name_start_position:]
    



def get_pid(process_name):
    global pids

    log_handler =  logger.get_logger("pid.log")
    a = os.popen('ps -ef | grep {}'.format(process_name)).readlines()

    filter_1 = "grep"
    filter_2 = "python"
    for x in a:
        try:
            if (x.find(filter_1) != -1) or (x.find(filter_2) != -1) :
                log_handler.info("escaped")
                pass
            else:
                #log_handler.info(x)
                add_to_dict(x)
                #pids.append(int(x[10:15]))
                #process[int(x[10:15])] = x[49:]
        except Exception as inst:
            #print inst
            pass

    #return the list if not null
    if not pids:
        return -1
    else: 
        return pids


# main function

if __name__ == "__main__":
    if (len(sys.argv)>=2):
       process_name = sys.argv[1]
       get_pid(process_name)
    else:
        usage()
