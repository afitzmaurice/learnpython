def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers." % boxes_of_crackers
    print "Get a blanket.\n"

print "We can give the function numbers directly:"  
cheese_and_crackers(20, 30)

print "Or, we can use variables from our script:" #ie define local variables to pass
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

#variables in your function are not connected to the variables in your script
#function takes numbers, variables, math or all three
