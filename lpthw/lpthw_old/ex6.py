x = "There are %d types of people." % 10 # first sentence
binary = "binary" #just a string(word)
do_not = "don't" # just a string(word)
y = "Those who know %s and those who %s." % (binary, do_not) # second sentence

print x # print as is
print y # prints as is

print 'I said: %s.' % x # print with r - repr
print "I also said: '%s'." % y # print with s - string

hilarious = False # print boolean value
joke_evaluation = "Isn't that joke so funny?! %r" # print str with 

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e