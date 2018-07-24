from sys import argv #import module

script, filename = argv # assing valuable

print "We're going to erase %r." % filename # print filname
print "If you don't want that, hit CTRL-C (^C)." #aborting
print "If you do wan that, hit RETURN." #continue

raw_input("?") #...

print "Opening the file..." #prining
target = open(filename, 'w') # assing to "target" opened file

print "Truncating the file. Goodbye!"
target.truncate() #erasing opened file

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ") # 3 lines assigning 
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write("%s\n%s\n%s\n" % (line1,line2,line3))
#target.write("{0}\n{1}\n{2}".format(line1,line2,line3))
#target.write(line1) # 3 lines writing
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print "And finally, we close it."
target.close() #closing file
