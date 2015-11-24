#turn while loop into a function

def create_list(length):
    list = range(int(length))
    print list

print "How long is your list?"
length = raw_input('> ')

create_list(length)

#initial while loop from exercise 33
i = 0
numbers = []  #create empty list. note: must be created outside while loop.

while i < 6:
    print "The top i is %d" % i
    numbers.append(i) #add the current i value to numbers list
    
    i += 1   #increment i so that the while loop eventually ends
    print "Numbers now: ", numbers  #shows the list after each iteration of loop
    print "Bottom i is %d" % i #shows i at end of each iteration of loop

print "The numbers: "

for num in numbers:
    print num

print "The while loop above can also be replaced with a for loop:"

numbers = []

for i in range(0, 6):
    numbers.append(i)

print numbers

print "Or just create a list with range 0 to 5:"
    
#can also create a list with numbers 0:5 by the following
list = range(6)
print list
