#!/usr/bin/env python

import sys
import os
import time
import subprocess
from itertools import islice

__all__ = ['PROCCPU','get_cpu_usage']

_instance = None

def _get_instance(pid='None'):
	global _instance
	if _instance is None:
		_instance = PROCCPU(pid)
	return _instance
	
def get_cpu_usage():
	return _get_instance().get()


class  PROCCPU(object):
	"""docstring for  CPUUSage"""
	def __init__(self, pid):
		self.pid = pid
		self.stat_path = "/proc/"+pid+"/stat"

	def get(self):
		return self.parse_process_cpu_usage(self.read_process_cpu_usage(self.stat_path))
	__call__ = get		

	@staticmethod
	def read_process_cpu_usage(stat_path):
    with open(stat_path) as stat_file:
    	return next(stat_file)

    @staticmethod
	def parse_process_cpu_usage(cpu_stat_line)
	token = cpu_stat_line.split()
	utime = token[13] 
	stime = token[14]  
    return (utime,stime)



