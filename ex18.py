def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#this takes only one argument
def print_one(arg1):
    print "arg1: %r" % arg1

#this takes no arguments
def print_none():
    print "Nothing here."

print_two("Ba","boo")
print_two_again("Baba","loo")
print_one("First!")
print_none()
