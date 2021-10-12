import time

def calculate_time(func):
	''' Takes in a function that will be used by the wrapper.'''
	def wrapper():
		''' Saves the time that the function took to run.
		    Returns 'Total time X', X being the time.
		'''
		# By using the time.time(), I can get the current time in seconds.
		A = time.time()
		func()
		B = time.time()
		'''
		By storing the time in seconds before and after calling the function,
		and by subtracting the time before from the time after, we can find the
		total time that the function used.
		'''
		X = B - A
		print(f'Total time {X}')
	return wrapper
