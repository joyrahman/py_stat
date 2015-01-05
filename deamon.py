import proc_to_pid
import sys
import collect_stat as proc_data
import threading
import logging
import time
from Queue import Queue

logging.basicConfig(level=logging.DEBUG,\
        format='[%(levelname)s] (%(threadName)-10s) %(message)s',)


threads = []
pid_queue = Queue()
'''
def worker(pid, proc_name, timer=120):
    logging.debug('Starting')
    proc_data.get_stat(str(pid), proc_name, timer)
    logging.debug('Ending')

'''

def worker(pid, proc_name, timer = 120):
    i = pid
    while True:
        pid = pid_queue.get()
        logging.debug('starting')
        proc_data.get_stat(str(pid), proc_name, timer)
        logging.debug('Ending')
        time.sleep(i + 2)
        pid_queue.task_done()


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
    proc_name = "apache"
    timer =  13
    number_of_worker =  3

    # get the matching pids to proc_name
    pids =  proc_to_pid.get_pid(proc_name)
    # insert the items to queue
    for pid in pids:
        pid_queue.put(pid)


    # Set up some threads to fetch the enclosures
    for i in range(number_of_worker):
        t_worker = threading.Thread(target=worker, args=(i, pid_queue,timer))
        t_worker.setDaemon(True)
        t_worker.start()



    # Now wait for the queue to be empty, indicating that we have
    # processed all of the downloads.
    print '*** Main thread waiting'
    pid_queue.join()
    print '*** Done'

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

    
