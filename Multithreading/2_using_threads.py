# USING THREADS
import threading
import time

start = time.perf_counter()

# dummy function
def do_something():
	print("Sleeping 1 second...")
	time.sleep(1)
	print("Waking up...")

# initiating thread 1
t1 =  threading.Thread(target = do_something)
t1.start()

# initiating thread 2
t2 =  threading.Thread(target = do_something)
t2.start()

# joining all threads
t1.join()
t2.join()

"""
The join() method avoids running main function concurrently with the threads.
In other words join() methods suspends the main thread until the generated threads are done executing.
Comment lines 22 and 23 to see the difference
"""

finish = time.perf_counter()

print("Finished in {} seconds".format(round(finish - start, 2)))