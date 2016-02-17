i = 0
numbers = []

while i < 6:
	print "A the top i is %d" % i
	numbers.append(i)
	
	i = i + 1
	print "numbers now: ", numbers
	print "At the bottom i is %d" % i
	
	
print "THe numbers: "

for num in numbers:
	print num
	