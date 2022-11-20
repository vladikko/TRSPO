#Implement the calculation of numbers in accordance with the Collatz conjecture, using parallel computing approaches.

import random
import threading
import time
from queue import Queue
import os

N = 10000

class Collatz:
    def __init__(self, num):
        self.num = num
        self.steps = 0
        self.initialNum = num
    def getNum(self):
        return self.num
    def getSteps(self):
        return self.steps
    def setNum(self, num):
        self.num = num
    def setSteps(self, steps):
        self.steps = steps
    def getInitialNum(self):
        return self.initialNum

def collatz_calc(num):
    if num % 2 == 0:
        return num // 2
    else:
        return 3 * num + 1

def collatzThread(queue, solved):
    while not queue.empty():
        collatz = queue.get()

        collatz.setNum(collatz_calc(collatz.getNum()))
        collatz.setSteps(collatz.getSteps() + 1)

        if(collatz.getNum() == 1):
            solved[collatz.getInitialNum()-1] = collatz
        else:
            queue.put(collatz)

def main():
    q = Queue()
    solved = [None] * N
    for i in range(N):
        q.put(Collatz(N-i))

    threads = []
    cpu_count = os.cpu_count()
    print(cpu_count)
    start_time = time.time()
    for i in range(os.cpu_count()):
        t = threading.Thread(target=collatzThread, args=(q, solved))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    # for i in range(len(solved)):
    #     print("Number: " + str(solved[i].getInitialNum()) + " Steps: " + str(solved[i].getSteps()))

    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()