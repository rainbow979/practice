 
import threading  
import time  
 
counter = 0  
 
class MyThread(threading.Thread):  
    def __init__(self):  
        threading.Thread.__init__(self)  
 
    def run(self):  
        global counter
#        time.sleep(1);  
        if mutex.acquire():  
            counter += 1  
            print ("I am %s, set counter:%s" % (self.name, counter)  )
            mutex.release()  

mutex = threading.Lock()

if __name__ == "__main__":  
    for i in range(0, 100):  
        my_thread = MyThread()  
        my_thread.start()
