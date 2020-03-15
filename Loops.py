For Loops


#The continue Statement - stop the current iteration

fruits = ["apple", "banana", "orange", "pinapple", "coconut", "cucumber"]
for x in fruits:
	if x == "pinapple":
		pass
	print(x)

for x in fruits:
	if x == "pinapple":
		pass
	print(x)

for x in fruits:
	if x == "pinapple"
		pass
	print(x)


#The range()  Funtion - a set of code a specified number of times

for x in range(10):
	print(x)

for x in range(10, 100):
	print(x)

for x in range(10, 100, 5)
	print(x)



#Nested Loops

NumberA = [1, 2, 3, 4, 5]
NumberB = [1, 2, 3, 4, 5]

for x in NumberA:
	for y in NumberB:
		print(x,y)



#pass

for in [1, 2, 3, 4, 5]
	pass


-----------

words = ['cat', 'window', 'defenstrate']
for w in words:
	print(w, len(w))


-----------
for n in range(2, 10):
	for x in range(2, n):
		if n % x == 0:
			print(n, 'equal', x, '*', n//x)
			break
	else:
		# loop fell through without finding a factor
		print(n, 'is a prime number')



-----------

for num in range(2, 10):
	if num % 2 == 0:
		print("Found an evev number", num)
		continue
	print("Found a number", num)


-----------
>>> Fibonacci #module Folder