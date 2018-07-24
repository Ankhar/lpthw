def lifed1(money, work):
	hp = money / work
	print "You have %r money, and %r hours work" % (money, work)
	print "Your hp is %r" % (hp)

lifed1(10000,10)
print "work hard"

job = 10
cash = 30000
lifed1(cash,job)
print "with my script, you"


lifed1(30+10000, 4+4+4)
print "And with even without you"

lifed1 (300000+cash, job +14)
print "And without even the Earth"

print "or on your own"
cash = int(raw_input("amount of cash "))
job = int(raw_input("hours "))
lifed1(cash, job)