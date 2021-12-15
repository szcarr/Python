import threading
import time

threads = []

def seiHei():
    print("Hei")
    time.sleep(3)
    print("sann")

for i in range(100):
    t = threading.Thread(target=seiHei)
    t.daemon = True
    threads.append(t)

for i in range(100):
    threads[i].start()
    time.sleep(1)

for i in range(100):
    threads[i].join()