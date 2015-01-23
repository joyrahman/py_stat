import psutil
import statsd
import time
import sys

def send_stat():
    gauge1 = statsd.Gauge('CPU')
    gauge1.send('cpu_percent',psutil.cpu_percent())
    gauge1.send('mem_utilization',psutil.virtual_memory().percent)

def main():
    try:
        interval = 1
        while True:
            send_stat()
            time.sleep(interval)
    except (KeyboardInterrupt, SystemExit):
        print ("Interrupted")
        sys.exit()


if __name__ == '__main__':
    main()
