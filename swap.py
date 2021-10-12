def swap_last_item(myList):
	'''Takes in a list, swaps the first and last element.
	   Returns the new list.
	'''
	# x will hold a copy of the last element, so it is not lost when I put first element in the last index.
	x = myList[-1]
	myList[-1] = myList[0]
	myList[0] = x
	return myList
