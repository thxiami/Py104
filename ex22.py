def add(a,b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "Subtracting %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	print "a:",a, "b:",b
	return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100.3, 2)

print "Age: %d,\nHeight: %d, \nWeight: %d,\nIQ: %d" %(age, height, weight,iq)

#PUZZLE
print "Here is a puzzle."

what = add(age,subtract(height, multiply(weight, divide(iq,2))))

print "That becomes:", what, "Can you do it by hand?"