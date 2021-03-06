import proc_to_pid
import sys
import collect_stat as proc_data
import threading
import logging
import time
import SetQueue
#from Queue import Queue

logging.basicConfig(level=logging.DEBUG,\
        format='[%(levelname)s] (%(threadName)-10s) %(message)s',)


#threads = []
pid_queue = SetQueue.SetQueue()
'''
def worker(pid, proc_name, timer=120):
    logging.debug('Starting')
    proc_data.get_stat(str(pid), proc_name, timer)
    logging.debug('Ending')

'''
def in_queue(item):
    global pid_queue
    return item in pid_queue

def queue_injector(proc_name, timer=120):
    global pid_queue
    pid_list = {}
    try:
        while threading.current_thread().signal:
	    print ".",
            # get the matching pids to proc_name
            pids =  proc_to_pid.get_pid(proc_name)
            # insert the items to queue
            #print pids 
            # the process exist
            if pids != -1:
                for pid in pids:
                    # if the pid is not already in Queue, append it
                    #if not in_queue(pid):
                    if not pid in pid_list.keys():
                        pid_queue.put(pid)
                        pid_list[pid] = True
                    
                #print "Queue:", pid_queue
            	#time.sleep(1)
	        # the process does not exist
            #elif pids == -1:
		    time.sleep(1)
            #time.sleep(1)
    except Exception as Inst:
        print Inst
        print "Got some Error in Queue Injector"


def worker(pid, proc_name, timer = 120):
    i = pid
    try:
        while threading.current_thread().signal:
            # wait until the queue has some elements
            pid = pid_queue.get()
            print "pid: " + str(pid)
            logging.debug('starting')
            proc_data.get_stat(str(pid), proc_name, timer)
            logging.debug('Ending')
            #time.sleep(i + 2)
            pid_queue.task_done()
    except Exception as Inst:
        print "Got some Error as worker"

def run_threads(pids):
    #threads = []
    global threads
    for t in threads:
        print t
    for pid in pids:
        thread_name = "{}-{}".format(str(pid), proc_name)
        if thread_name in threading.enumerate():
            print "Thread Exist"
        else:
            t = threading.Thread ( name = thread_name, target = worker, args = ( pid, proc_name, timer ))
            threads.append(t)
            t.start()
    #return threads    


def pid_exist(proc_name):
    pids = proc_to_pid.get_pid(proc_name)
    if pids is null:
        return false
    else:
        return true


def main():

    ''' parameters '''
    proc_name = "zerovm"
    timer =  120
    number_of_worker =  10
    threads = []
    # get the matching pids to proc_name
    #pids =  proc_to_pid.get_pid(proc_name)
    # insert the items to queue
    #for pid in pids:
    #    pid_queue.put(pid)

    # thread to insert data to Queue

    data_injector = threading.Thread(target=queue_injector, args=( proc_name, timer))
    data_injector.setDaemon(True)
    data_injector.signal = True
    data_injector.start()
    threads.append(data_injector)
    # Set up some threads to fetch the enclosures
    for i in range(number_of_worker):
        t_worker = threading.Thread(target=worker, args=( i, pid_queue,timer))
        t_worker.setDaemon(True)
        t_worker.signal = True
        t_worker.start()
        threads.append(t_worker)



    # Now wait for the queue to be empty, indicating that we have
    # processed all of the downloads.
    try:
        while True:
            print '*** Main thread waiting'
            #pid_queue.join()
            #print '*** Done'
            time.sleep(50)
    except KeyboardInterrupt:
        print "Exiting"
        for t in threads:
            t.signal = False
            print "Exit of Thread", t.getName()

    '''
    if pid is not null, then insert the pid to the queue
    '''
    '''
    if (pid !=-1) and q.empty():
        for item in pid:
            q.put(item)
    '''
  

if __name__ == "__main__":
    
    main()
    
#     '''
#     proc_name = "apache"
#     timer =  13
#     if len(sys.argv)>=2:
#         proc_name = sys.argv[1]
#     thread_running =  False
#     try:
#         while (True):
#             pids = proc_to_pid.get_pid(proc_name)
#             if (pids != -1)  and (thread_running == False) :
#                 thread_running = True
#                 #thread_list = run_threads(pids)
#                 run_threads(pids)
#                 #main_thread = threading.currentThread()
#                 time.sleep(2*timer)
#                 '''
#                 # this section is disabled
#                 '''
#                 for t in threading.enumerate():
#                     if t is main_thread:
#                         continue
#                     logging.debug('joining %s', t.getName())
#                     t.join()
#             elif pids!= -1 and thread_running == True:
#                 print "pass"
#                 if threading.active_count() == 1:
#                     thread_running = False
#                  '''
#             #temporary disabled
#
#             '''
#             else:
#                 #thread_running = False
#                 if threading.active_count() == 1:
#                     thread_running = False
#                 time.sleep(1)
#
#     except KeyboardInterrupt:
#         print "Existing"
#         #sys.exit()
#     except Exception as Inst:
#         print Inst
#
#     finally:
#         main_thread = threading.currentThread()
#         for t in threading.enumerate():
#             if t is main_thread:
#                 continue
#             logging.debug('joining %s', t.getName())
#             t.join()
#     '''
# '''
#     # list of existing pids
#     pids = proc_to_pid.get_pid(proc_name)
#
#
#
#     #threaded execution may be needed for each pid
#     threads = []
#     for pid in pids:
#         thread_name = "{}-{}".format(str(pid), proc_name)
#         t = threading.Thread(name= thread_name, target=worker,\
#                 args=(pid, proc_name, timer))
#         threads.append(t)
#         t.start()
#
#
#     # single threaded implementation
#     #pid = pids[0]
#     #proc_data.get_stat(str(pid), proc_name, 13)
# '''

    
