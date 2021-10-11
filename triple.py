def tripler(func):
	''' Takes in a function that will be used by the wrapper, calls the function thrice.
                Returns func's output thrice.
	'''
	func()
	func()
	func()
