the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for loop goes through a list
#note that number is defined by the for loop when it starts
for number in the_count:
    print "This is count %d" % number

#same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

#note that we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

#we can also build lists, first start with an empty one
elements = []

#then use the range function to do 0 to 5 counts
#note that the range does not include the last number, in this case, '6'
for i in range(0, 6):
    print "Adding %d to the list" % i
    #append is a function that lists understand
    elements.append(i)

#the above for loop can be replaced with "elements = range(6)"

#now we can use the for loop to print them as well
for i in elements:
    print "Element was: %d" % i
