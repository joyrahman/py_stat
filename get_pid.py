import os

pids = []
process = {}
a = os.popen('ps -ef | grep "chromium"').readlines()

for x in a:
    #print x 
    try:
        pids.append(int(x[10:15]))
        process[int(x[10:15])] = x[49:]
    except:
        print ":( "
        pass
for each in pids:
    print(each)

for key in process:
    print key,"=>",process[key]
