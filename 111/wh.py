import threading

def write():
    print("qqq")

thread1 = threading.Thread(target=write)
thread2 = threading.Thread(target=write)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
