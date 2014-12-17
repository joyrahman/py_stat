
from process_cpu_stat import PROCCPU as process
from system_cpu_stat import SYSTEMCPU as system






def main():
	pid = "1014"
	proc = process(pid)
	print proc.get_cpu_usage()
	sys = system()
	print sys.get_cpu_usage()
	





if __name__ == '__main__':
	main()



