number = 1
last = 0
before_last = 0

for counter in range(0,10):
	before_laste = last
	last = number
	number = before_last + last
	print (number)
