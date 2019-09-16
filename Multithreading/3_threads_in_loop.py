# USING lOOPS
import threading
import time

start = time.perf_counter()

# dummy function
def do_something(seconds):
	print("Sleeping {} seconds...".format(seconds))
	time.sleep(seconds)
	print("Done Sleeping")

# an empty list to append all threads
threads = []

# for loop to generate 10 threads
for _ in range(10):
	t =  threading.Thread(target = do_something, args=[1.5]) # use args to pass arguments to the target function
	t.start()
	threads.append(t)

"""
Joining threads in the same loop makes threading redundant,
beacause it will wait for the thread to complete before moving to the next iteration
In other words, it will be the same as running the code synchronously
"""

# for loop to join the appended threads
for thread in threads:
	thread.join()
	

finish = time.perf_counter()

print("Finished in {} seconds".format(round(finish - start, 2)))
