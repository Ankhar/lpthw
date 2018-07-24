from sys import argv # import module(argv from a package(sys))

script, filename = argv # parameters

txt = open(filename) # open file(parameter)

print "Here's your file %r:" % filename #just print a string
print txt.read() # read file(parameter)
close(txt)
print "Type the filename again:" # prompt to type the filename again
file_again = raw_input("> ") # input and new parameter

txt_again = open(file_again) # rename again, new2 parameter

print txt_again.read() # print new2 parameter
close(txt_again)