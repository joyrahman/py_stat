import os
import sys

pids = []
process = {}

def usage():
    print 'python get_pid.py <process_name>'
    sys.exit(1)
                         
def add_to_dict(x):
    global pids 
    global process
    pids.append(int(x[10:15]))
    process[int(x[10:15])] = x[49:]
    print process

# main function

if __name__ == "__main__":
    main()


def main():
    if (len(sys.argv)>=2):
       process_name = sys.argv[1]
    else:
        usage()
    a = os.popen('ps -ef | grep {}'.format(process_name)).readlines()
    #a = os.popen('ps -ef').readlines()

    filter_1 = "grep"
    filter_2 = "python"
    for x in a:
    #    print x 
        try:
            if (x.find(filter_1)) != -1 or x.find(filter_2) !=1:
                pass
            else:
                add_to_dict(x)
                #pids.append(int(x[10:15]))
                #process[int(x[10:15])] = x[49:]
        except:
            #print ":( "
            pass
    #for each in pids:
    #    print(each)

    for key in process:
        print key,"=>",process[key]
