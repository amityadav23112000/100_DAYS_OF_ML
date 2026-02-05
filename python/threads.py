#multithreading in python
import threading
from time import sleep , time

# lock = threading.Lock()
# lock.equire()
#reer




def helper():
    sleep(1)
    print("this is helper function")
            

if __name__ == "__main__":
    # t1= threading.Thread(target=helper)
    # t2 = threading.Thread(target=helper)
    start_time= time()
    # t2.start()
    # t1.start()
    # t1.join()
    # t2.join()
    threads = [ threading.Thread(target=helper) for _ in range(5) ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    end_time= time()
    print("time taken :", end_time - start_time)
    print("this is main function")