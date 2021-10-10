def tripler(func):
	''' Takes in a function that will be used by the wrapper.
	'''
	def wrapper():
		''' Calls the function thrice.
                	Returns func's output thrice.
		'''
		func()
		func()
		func()
	return wrapper
