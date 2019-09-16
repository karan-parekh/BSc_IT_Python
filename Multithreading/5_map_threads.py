# USING MAP METHOD ON THREADS

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
	# variable to store the list of results returned by the map method 
	results = executor.map(do_something, seconds) # map returns a list of results

	# for loop to print the results
	for result in results:
		print(result)

finish = time.perf_counter()

print("Finished in {} seconds".format(round(finish - start, 2)))
