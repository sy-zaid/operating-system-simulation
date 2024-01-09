import easygui
import threading
import random,time

data = [random.randint(1, 100) for i in range(10)]
result = [0] * len(data)

def sorting_thread(start, end,threadno):
    
    
    result[start:end] = sorted(data[start:end]) # Slicing the provided list.
    easygui.msgbox(f"""Thread-{threadno} started!\nData list for sorting: {data}\n
This thread is sorting elements from index {start} to {end}\n\n
Sorted elements: {result[start:end]}""")

def sortByTwoThreads():
    """
    Function to create two threads at a time, simulating multithreading in an OS.

    """
    mid = len(data) // 2 # dividing num of elements in two.
    thread1 = threading.Thread(target=sorting_thread, args=(0, mid,1))
    thread2 = threading.Thread(target=sorting_thread, args=(mid, len(data),2))

    thread1.start()
    thread2.start()

    thread1.join() #Waiting for all the threads to be completed.
    thread2.join()

    global result
    result = sorted(result)

if __name__ == "__main__":
    print("Original List:", data)

    sortByTwoThreads()

    print("Sorted List:", result)
