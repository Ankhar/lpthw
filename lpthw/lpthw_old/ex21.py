def add(a,b):
	print "ADDING %d + %d" % (a,b)
	return a+b

def subtract(a,b):
	print "SUBTRACTING %d - %d" % (a,b)
	return a - b
	
def multiply(a,b):
	print "MULTIPLYING %d * %d" % (a,b)
	return a * b
	
def divide(a,b):
	print "DIVIDING %d / %d" % (a,b)
	return a / b
	

print "Let's do some math just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100,2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


#A puzzle for extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes : ", what, "Can you do it by hand?"

what1 = float(divide(age, multiply(weight,add(height, subtract(iq, 10)))))

print "That's awesome!", what1

print "Now try that: 24+40/10*2"

what2 = float(add(24, multiply(2, divide(40,10))))
controlwhat2 = 24+40/10*2

print "Your result is: %d and right result is: %d" % (what2, controlwhat2)

