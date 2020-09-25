# Problem Statement 2: MultiThreading
# ● Write a python code to do the following:
# ○ It should be able to launch 3 different thread
# ○ Each thread should print this every 5 second:
# ■ Thread <thread number> is running at <time elapsed>
# ■ E.g.
# ● "Thread 2 is running at 0"
# ● "Thread 2 is running at 5"
# ● "Thread 2 is running at 10"

# ○ Initially start thread 1 and 3
# ○ After 20 second stop thread 1 start thread 2
# ○ Again after 18 second stop thread 3 and start thread 1
# ● Deliverables
# ○ Code in Python

from threading import *
import time

start = time.time()


class Thread1(Thread):
    def run(self):
        end = time.time()
        print("Thread 1 is running at ", int(end-start))


class Thread2(Thread):
    def run(self):
        end = time.time()
        print("Thread 2 is running at ", int(end-start))


class Thread3(Thread):
    def run(self):
        end = time.time()
        print("Thread 3 is running at ", int(end-start))


while(True):
    end = time.time()
    
    if(int(end-start)%5==0):
        
        if(int(end-start)<20):
            t1=Thread1()
            t3=Thread3()
            t1.start()
            t3.start()
            time.sleep(1)
        elif(int(end-start)>20 and int(end-start)<38):
            t3=Thread3()
            t2=Thread2()
            t3.start()
            t2.start()
            time.sleep(1)
        else:
            t1=Thread1()
            t2=Thread2()
            t1.start()
            t2.start()
            time.sleep(1)
 