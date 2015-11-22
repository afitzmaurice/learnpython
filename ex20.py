from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "Let's print the entire file:\n"
print_all(current_file)

print "Now let's rewind.\n"
rewind(current_file)

print "And then print lines from the file.\n"
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1  #this is equal to current_line += 1
print_a_line(current_line, current_file)

current_line += 1                #relates to line_count in that says add 1 to previous
print_a_line(current_line, current_file)

