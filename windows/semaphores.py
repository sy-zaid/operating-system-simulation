import threading
import random
import time

buf = []
empty = threading.Semaphore(1)
full = threading.Semaphore(0)
mutex = threading.Lock()


def producer():
    nums = range(5)
    global buf
    if len(buf) < len(nums):
        num = random.choice(nums)
        empty.acquire()
        mutex.acquire()  # added
        buf.append(num)
        print("Produced", num, buf)
        mutex.release()  # added
        full.release()
        time.sleep(1)
    else:
        mutex.acquire()


def consumer():
    global buf
    full.acquire()
    mutex.acquire()  # added
    num = buf.pop(0)
    print("Consumed", num, buf)
    mutex.release()  # added
    empty.release()
    time.sleep(2)


def writer():
    global buf
    global mutex

    # Writing...
    num = random.randint(1, 10)
    mutex.acquire()
    buf.append(num)
    print("Produced", num, buf)
    mutex.release()


def reader():
    global buf
    global mutex

    # Reading...
    mutex.acquire()
    if len(buf) > 0:
        num = buf.pop(0)
        print("Consumed", num, buf)
    mutex.release()


producerThread1 = threading.Thread(target=producer)
consumerThread1 = threading.Thread(target=consumer)
producerThread2 = threading.Thread(target=producer)
consumerThread2 = threading.Thread(target=consumer)
producerThread3 = threading.Thread(target=producer)
consumerThread3 = threading.Thread(target=consumer)
producerThread4 = threading.Thread(target=producer)
consumerThread4 = threading.Thread(target=consumer)
producerThread5 = threading.Thread(target=producer)
consumerThread5 = threading.Thread(target=consumer)
producerThread6 = threading.Thread(target=producer)
consumerThread6 = threading.Thread(target=consumer)


consumerThread1.start()
producerThread1.start()

consumerThread2.start()
producerThread2.start()

consumerThread3.start()
producerThread3.start()


