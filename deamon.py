import proc_to_pid as pid
import sys



if __name__ == "__main__":
    proc_name = "apache"
    if len(sys.argv)>=2:
        proc_name = sys.argv[1]
    pids = pid.get_pid(proc_name)
    print pids

    #threaded execution may be needed for each pid
