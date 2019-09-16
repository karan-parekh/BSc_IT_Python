# THREAD POOL EXECUTOR

import concurrent.futures 
import time

start = time.perf_counter()

# dummy function
def do_something(seconds):
	print("Sleeping {} seconds...".format(seconds))
	time.sleep(seconds)
	return "Done Sleeping for {} seconds".format(seconds)

# context manager for pooling threads
with concurrent.futures.ThreadPoolExecutor()  as executor:
	seconds = [5, 4, 3, 2, 1]	# list of args
	results = [executor.submit(do_something, sec) for sec in seconds] # submit method returns the future object

	"""
	A future object encapsulates the execution of our function
	which also allows us to check on it later
	(eg: if its running, done or check the result)
	"""

	# for loop to print results
	for f in concurrent.futures.as_completed(results):  # as_completed() methods yields the results as they are completed
		print(f.result())

finish = time.perf_counter()

print("Finished in {} seconds".format(round(finish - start, 2)))
