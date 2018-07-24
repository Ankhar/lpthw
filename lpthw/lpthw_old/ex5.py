name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inces tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)
	
cm_per_inch = 2.54 # cm in inches
kg_per_lbs = 0.454 # pounds per kg

inch = height
lbs = weight

cm_end = cm_per_inch * inch
kg_end = kg_per_lbs * lbs

print"%d cm im %d inch" % (cm_end, inch)
print"%d kg in %d pounds" % (kg_end, lbs)