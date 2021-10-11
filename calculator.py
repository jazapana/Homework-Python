def calculator(number1, number2, operator):
	''' Takes in 2 numbers and an operator, and computes the result that depends on the operator.
		Returns the sum, difference, product, quotient, quotient without remainder,
		or power of the two numbers, or False if there are missing or incorrect parameters.
	'''
	# by using if else statements, the function will choose one of these statements, and return the following calculation, or False,
	# depending on the operator.
	if operator == '+':
		return number1 + number2
	elif operator == '-':
		return number1 - number2
	elif operator == '*':
		return number1 * number2
	elif operator == '/':
		if number2 == 0:
			return False
		return number1 / number2
	elif operator == '//':
		return number1 // number2
	elif operator == '**':
		return number1 ** number2
	else:
		return False

def parse_input():
	''' Asks user to enter an equation that has two numbers and an operator.
		Calls the calculator function using the user's input as parameters, or
		returns False if the input did not have two numbers and operator.
	'''
	theInput = input('Enter equation: ')
	inputString = theInput
	# by using if else statements, the function will choose one of the statements.
	# depending if the user's input contains a valid operator, by using the split method the function will
	# split the input into two numbers, and enters the numbers and operator into the calculator function, and prints it.
	# if the user's input does not contain a valid operator, the function returns False.
	if ' + ' in inputString:
		addInput = inputString.split('+')
		num1 = float(addInput[0])
		num2 = float(addInput[1])
		print(calculator(num1, num2, '+'))
	elif ' - ' in inputString:
		subInput = inputString.split('-')
		num1 = float(subInput[0])
		num2 = float(subInput[1])
		print(calculator(num1, num2, '-'))
	elif ' * ' in inputString:
		mulInput = inputString.split('*')
		num1 = float(mulInput[0])
		num2 = float(mulInput[1])
		print(calculator(num1, num2, '*'))
	elif ' / ' in inputString:
		divInput = inputString.split('/')
		num1 = float(divInput[0])
		num2 = float(divInput[1])
		print(calculator(num1, num2, '/'))
	elif ' // ' in inputString:
		intdInput = inputString.split('//')
		num1 = float(intdInput[0])
		num2 = float(intdInput[1])
		print(calculator(num1, num2, '//'))
	elif ' ** ' in inputString:
		powInput = inputString.split('**')
		num1 = float(powInput[0])
		num2 = float(powInput[1])
		print(calculator(num1, num2, '**'))
	else:
		return False
