import easygui
import threading
import random,time

data = [random.randint(1, 100) for i in range(10)]
# data = [53, 66, 71, 7, 42, 64, 65, 10, 96, 20]

result = [0] * len(data)
#  result = [0,0,0,0,0,0,0,0,0,0]

def sorting_thread(start, end,threadno):
    # Slicing in list
    result[start:end] = sorted(data[start:end]) # Slicing the provided list.

    easygui.msgbox(f"""Thread-{threadno} started!\nData list for sorting: {data}\n
This thread is sorting elements from index {start} to {end}\n\n
Sorted elements: {result[start:end]}""")

def sortByTwoThreads():
    """
    Function to create two threads at a time, simulating multithreading in an OS.

    """
    # data = [53, 66, 71, 7, 42,][ 64, 65, 10, 96, 20]
    mid_index = len(data) // 2 # index dividing num of elements in two.
    print(mid_index)
    thread1 = threading.Thread(target=sorting_thread, args=(0, mid_index,1))
    thread2 = threading.Thread(target=sorting_thread, args=(mid_index, len(data),2))

    thread1.start()
    thread2.start()

    thread1.join() # Waiting for all the threads to be completed.
    thread2.join()

    global result
    result = sorted(result)

if __name__ == "__main__":
    print("Original List:", data)

    sortByTwoThreads()

    print("Sorted List:", result)
