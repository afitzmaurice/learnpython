print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")
#if user enters "1", then give user two options when faced with the bear.
if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake.\n2. Scream at the bear."
#take input (1, 2, or something else) and assign to bear
    bear = raw_input("> ")
#if bear is 1 (user takes cake) then tell user that bear eats user's face   
#if bear is 2 then tell user bear eats user's legs
#if bear is something other than 1 or 2, tell user their response is better 
    if bear == "1":
        print "The bear eats your face. Good job!"
    elif bear == "2":
        print "The bear eats your legs off."
    else: 
        print "Well, doing %s is probably better. Bear runs away." % bear
#if user enters "2", then give user three options 
elif door == "2":
    print "You stare into the endless abyss."
    print "1. Blueberries\n2. Yellow jacket clothespins.\n3. Understanding melodies."
#assign user's input (1, 2, or something else) to insanity    
    insanity = raw_input("> ")
#if 1 or 2 then tell user he survives. if other than 1 or 2, tell user else statement.
    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello."
    else: 
        print "The insanity rots your eyes into a pool of muck."

else:
    print "You stumble around and fall on a knife and die. Good job!"
