#Any program that uses threading

import threading
import time

def thread1():
    while True:
        print("Thread 1")
        time.sleep(1)

def thread2():
    while True:
        print("Thread 2")
        time.sleep(2)

def main():
    t1 = threading.Thread(target=thread1)
    t2 = threading.Thread(target=thread2)
    t1.start()
    t2.start()

if __name__ == "__main__":
    main()