from sys import exit

prompt = ('>>> ')

def start():
	print "Where am I... What a messy place..."
	third_room()

def dead():
	print "You are dead."
	exit(0)
	
def third_room():	
	print "You are welcome. Joke! You are obviously not.(Wanna come closer Y\N?)"
	next = raw_input(prompt)
	if next == 'Y':
		print "You can take so much money as you want, only type how much..."
		next = input(prompt)
		if next > 0:
			print "Too much for you, so you are..."
			dead()
		elif next == 0:
			print "You can get home alive now...."
		else: 
			print 'WRONG'
			dead()
	else:
		print "You know what that was wrong?"
		dead()
		
start()