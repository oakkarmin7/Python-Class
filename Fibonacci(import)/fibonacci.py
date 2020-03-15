#Fibonacci


#fibonacci numbers module

#n = int(input('Pleae enter a number:'))

def fib(n):		#write Fiboncci series up
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a+b
	print()

#Go to Fibonacci powerpoint

def fib2(n):	#return Fibonacci series up to 
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a+b
	return result