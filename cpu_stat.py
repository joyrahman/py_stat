#!/usr/bin/env python

import sys
import os
import time
import subprocess
from itertools import islice



def read_system_cpu_usage(stat_path='/proc/stat'):
    with open(stat_path) as procfile:
        cputimes = procfile.readline()
        return sum(float(time) for time in cputimes.split()[1:])