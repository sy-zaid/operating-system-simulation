import easygui
import threading
import random,time



def sorting_thread(data,start, end,threadno):    
    global result
    # Slicing in list
    result[start:end] = sorted(data[start:end]) # Slicing the provided list.

    easygui.msgbox(f"""Thread-{threadno} started!\nData list for sorting: {data}\n
This thread is sorting elements from index {start} to {end}\n\n
Sorted elements: {result[start:end]}""")

def sortByTwoThreads(lststartend):
    """
    Function to create two threads at a time, simulating multithreading in an OS.
    """
    data = [random.randint(lststartend[0],lststartend[1]) for i in range(10)]
    # data = [53, 66, 71, 7, 42, 64, 65, 10, 96, 20]
    global result
    result = [0] * len(data)
    #  result = [0,0,0,0,0,0,0,0,0,0]
    
    mid_index = len(data) // 2 # index dividing num of elements in two.
    
    thread1 = threading.Thread(target=sorting_thread, args=(data,0, mid_index,1))
    thread2 = threading.Thread(target=sorting_thread, args=(data,mid_index, len(data),2))

    thread1.start()
    thread2.start()

    thread1.join() # Waiting for all the threads to be completed.
    thread2.join()

    result = sorted(result)
    easygui.msgbox(f"This is the final Sorted Array: {result}")


