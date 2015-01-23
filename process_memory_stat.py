import os
#from psutil import virtual_memory


#_proc_status = '/proc/%d/status' % os.getpid()

_scale = {'kB': 1024.0, 'mB': 1024.0*1024.0,
          'KB': 1024.0, 'MB': 1024.0*1024.0}

def get_mem_usage(pid, mem_type='VmSize:', since = 0.0):
    proc_file = '/proc/{}/status'.format(pid)
    return _VmB(proc_file,mem_type) - since

def get_system_mem_size():
    #mem = virtual_memory()
    mem = 90000
    #return mem.total
    return mem

def _VmB(proc_file, VmKey):
    #global _proc_status, _scale
    global _scale
     # get pseudo file  /proc/<pid>/status
    try:
        fp = open(proc_file)
        v = fp.read()
        fp.close()
    except:
        return 0.0  # non-Linux?
     # get VmKey line e.g. 'VmRSS:  9999  kB\n ...'
    i = v.index(VmKey)
    v = v[i:].split(None, 3)  # whitespace
    if len(v) < 3:
        return 0.0  # invalid format?
     # convert Vm value to bytes
    return float(v[1]) * _scale[v[2]]

#below methods are depricated to meat the requiremens. left to further extending.
def memory(since=0.0):
    '''Return memory usage in bytes.
    '''
    return _VmB('VmSize:') - since


def resident(since=0.0):
    '''Return resident memory usage in bytes.
    '''
    return _VmB('VmRSS:') - since


def stacksize(since=0.0):
    '''Return stack size in bytes.
    '''
    return _VmB('VmStk:') - since 
