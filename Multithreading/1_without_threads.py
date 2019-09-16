# USING NO THREADS
import time

start = time.perf_counter()

# dummy function
def do_something():
	print("Sleeping 1 second...")
	time.sleep(1)
	print("Waking up...")

# function calls
do_something()
do_something()

finish = time.perf_counter()

print("Finished in {} seconds".format(round(finish - start, 2)))
