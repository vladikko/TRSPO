import threading
import time
import random

class Class1:
    def __init__(self, num):
        self.num = num
    def getNum(self):
        return self.num
    def setNum(self, num):
        self.num = num

class Class2:
    def __init__(self, num):
        self.num = num
    def getNum(self):
        return self.num
    def setNum(self, num):
        self.num = num

def thread1(lock):
    for i in range(0, k1):
        lock.acquire()
        try:
            num = random.uniform(0, 100)
            class1.setNum(class1.getNum() + num)
            num = random.uniform(0, 100)
            class2.setNum(class2.getNum() + num)
        finally:
            lock.release()

def thread2(lock):
    for i in range(0, k2):
        lock.acquire()
        try:
            num = random.uniform(0, 100)
            class2.setNum(class2.getNum() + num)
            num = random.uniform(0, 100)
            class1.setNum(class1.getNum() + num)
        finally:
            lock.release()

if __name__ == "__main__":
    lock = threading.Lock()
    n = random.randint(10, 20)
    k1 = random.randint(10000, 20000)
    k2 = random.randint(10000, 20000)
    class1 = Class1(0)
    class2 = Class2(0)
    threads = []
    for i in range(0, n):
        if i < n / 2:
            threads.append(threading.Thread(target=thread1, args=(lock,)))
        else:
            threads.append(threading.Thread(target=thread2, args=(lock,)))
    start_time = time.time()
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print("Execution time: %s seconds" % (time.time() - start_time))
    print("Class1: %s" % class1.getNum())
    print("Class2: %s" % class2.getNum())