print "Do you want an island where you can hike or sunbathe? Enter 'hike' or 'sunbathe'."

island = raw_input('> ').lower()  #this ensures that if user enters 'Hike' then script does not go to final else

if island == 'hike':
    print "Okay, which do you prefer: Atlantic or Pacific?"
    
    ocean = raw_input('> ').lower()

    if ocean == 'atlantic':
        print "Why not go to Tortola!"
    elif ocean == 'pacific':
        print "How about Kauai!"
    else:
        print "Or just go to %s" % ocean
elif island == 'sunbathe':
    print "Go to Mustique!"
else:
    print "Have fun on your own!" 
