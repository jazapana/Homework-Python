import time

def calculate_time(func):
	''' Takes in a function, saves the time that the function took to run.
		Returns 'Total time X', X being the time.
	'''
	# by using the time.time(), I can get the current time in seconds.
	X = time.time()
	print(f'Total time {X}')
