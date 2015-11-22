def add(a, b):
    print "Adding %d and %d" % (a, b)
    return a + b  #this line does the adding and returns the result

def subtract(a, b):
    print "Subtracting %d - %d." % (a, b)
    return a - b

def multiply(a, b):
    print "Multiply %d times %d." % (a, b)
    return a * b

def divide(a, b):
    print "Dividing %d / %d." % (a, b)
    return a / b

print "Let's do math with functions!"
print "What's your age?", 
age = float(raw_input()) #instead of creating age in script, ask user for their age
#age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d\nHeight: %d\nWeight: %d\nIQ: %d" % (age, height, weight, iq)
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
#what = -4391

print "That becomes: ", what
