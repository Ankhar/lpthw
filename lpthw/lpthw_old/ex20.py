from sys import argv #import

script, input_file = argv #assinging something

def print_all(f): #function with variable f ;\ 
	print f.read() #that will print after read

def rewind(f): # function that seek?
	f.seek(0)
	
def print_a_line(line_count,f): # main function
	print line_count, f.readline()
	#print only 1 line and count lines
	
current_file = open(input_file) # open

print "First let's print the whole file:\n"

print_all(current_file) #function that print f

print "\nNow let's rewind, kind of like a tape."

rewind(current_file) #function that seek(rewind)

print "Let's print three lines:\n"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)