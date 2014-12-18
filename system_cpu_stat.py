#!/usr/bin/env python

import sys
import os
import time
import subprocess
from itertools import islice

__all__ = ['SYSTEMCPU','get_cpu_usage']

_instance = None

def _get_instance():
    global _instance
    if _instance is None:
        _instance = SYSTEMCPU()
    return _instance

def get_cpu_usage():
    return _get_instance().get()


class  SYSTEMCPU(object):
    """docstring for  SYSTEMCPU"""
    def __init__(self, stat_path='/proc/stat'):
        self.stat_path = stat_path

    def get(self):
        return self.parse_system_cpu_usage(self.read_system_cpu_usage(self.stat_path))

    __call__ = get


    @staticmethod
    def read_system_cpu_usage(stat_path):
        with open(stat_path) as stat_file:
            output = stat_file.readline()
        return next(output)

    @staticmethod
    def parse_system_cpu_usage(cpu_stat_line):
        return sum(float(time) for time in islice(cpu_stat_line.split(),1,None))



