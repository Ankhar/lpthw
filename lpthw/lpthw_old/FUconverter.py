cm_per_inch = 2,54 # cm in inches
kg_per_lbs = 0,454 # pounds per kg

inch = input(float("Please, input amount of inches: "))
lbs = input(float("Please, input amount of pounds(lbs): "))

cm_end = cm_per_inch * inch
kg_end = kg_per_lbs * lbs

print "In ",inch," inches ",cm_end," cm."
print "In",lbs," pounds ",kg_end," kg."