import socket
import sys
from datetime import datetime
import threading
from queue import Queue

target_host = "127.0.0.1" 
ports_to_scan = range(1, 1025) 

print("-" * 50)
print(f"Scanning target: {target_host}")
print(f"Time started: {str(datetime.now())}")
print("-" * 50)


queue = Queue()
print_lock = threading.Lock()

def scan_port(target, port):
    try:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0) 
        
       
        result = s.connect_ex((target, port))
        if result == 0:
            with print_lock:
                print(f"[+] Port {port}: OPEN")
        s.close()
    except socket.error:
        pass

def threader():
    while True:
        worker = queue.get()
        scan_port(target_host, worker)
        queue.task_done()


for x in range(100):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()


for worker in ports_to_scan:
    queue.put(worker)


queue.join()

print("-" * 50)
print("Scanning completed!")
print("-" * 50)