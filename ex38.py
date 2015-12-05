#create ten things variable and assign a string
ten_things = "apples oranges crows telephone light sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ['day', 'night', 'song', 'frisbee', 'corn', 'banana', 'girl', 'boy']
#while stuff has less than ten items, add the last item from more_stuff
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now" % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."
#display second item in list stuff
print stuff[1]
#display last item in stuff
print stuff[-1]
print stuff.pop()
#remove the commas between the items and leave a space between items
print ' '.join(stuff)
#display item at location3 then # then item at location 4 (range 3:5 does not include 5)
#telephone#light
print '#'.join(stuff[3:5])
