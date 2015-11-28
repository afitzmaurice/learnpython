from sys import exit

i = 0

def ladera():
    print "huff\nhuff\nhuff\n"
    exit(0)

def nirvana(bliss):
    print "you have achieved nirvana!", bliss
    exit(0)

stores = ['Yard Dog', 'Stag', 'Kit and Ace']

def pick_store():
    choice = 'no'
    print "I'll give you some options and you say 'yes' or 'no':"
    while choice == 'no':
        for store in stores:
            print "Do you want to go to %s?" % store
            choice = raw_input('> ')
            if choice == 'yes':
                print "Okay, let's see if %s is open" % store
                exit(0)

print "In which area of Austin are you now: northwest, south, or eastside?"

area = raw_input('> ')

if 'northwest' in area:
    print "let's go for a run!"
    print "do you prefer hills or trails?"
    type = raw_input('> ')
    
    if type == 'hills':
        print "let's check out ladera norte."
        ladera()
    elif type == 'trails':
        print "go to bull creek."
        nirvana('you\'ve found your trail!')
    else: 
        print "not sure what that is. try again."
        start()
elif 'south' in area:
    print "there's good shopping around here."
    pick_store()
elif 'eastside' in area:
    print "let's eat! pizza or small bites?"
    food = raw_input('> ')
    if food == 'small bites':
        print 'go to qui'
        nirvana('food heaven')
    elif food == 'pizza':
        print 'you\'re going to have to earn that first. head to ladera'
        ladera()
    else:
        print 'not sure what that is.'
        exit(0)
else:
    print 'you are where?'
    nirvana('we all have our own private %s') % area

start()
