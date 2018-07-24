from sys import exit

prompt = ('>>> ')

def start():
	print "Where am I... What a messy place..."
	first_room()

def dead():
	print "You are dead."
	exit(0)
	
	
def first_room():
	print 'You can\'t see anything, too dark here.\nYou have a lantern, but it turn off.\nYou should write "turn on" if you want it'
	next = raw_input(prompt)
	
	if next == 'turn on':
		print 'So now you can see 2 doors, left and right'
		next_r = raw_input(prompt)
		if next_r == 'left':
			left_room()
		elif next_r == 'right':
			right_room()
	else:
		print 'You stumbled here for some time, but then was eaten by shadows.'
		
		
def left_room():
	print 'You have been eaten by a russian bear.'
	dead()
def right_room():
	print 'You see picture on the wall. There is a mobile with 2 buttons - A and B.\n What if you try to press one of them? Type "A" or "B"'
	next = raw_input(prompt)
	if next == 'A':
		print "Counter... 5...4..3..2..1.. BOOOOOOOM"
		dead()
	if next == 'B':
		third_room()
	else: 
		print "You have no time to make mistakes, so..."
		dead()
		
		
def third_room():
	print "You are welcome. Joke! You are obviously not.(Wanna come closer? Type Y or N?)"
	next = raw_input(prompt)
	if next == 'Y':
		print "You can take so much money as you want, only type how much (Put value from 0 to infinite)..."
		next = raw_input(prompt)
		if next > 0:
			print "Too much for you, so you are..."
		if next == '0':
			print "You can get home alive now...."
		if next == 'infinite':
			print "OH DAMN U MOTHERFUCKER BLACK HOLES EAT YOU"
			dead()
		else: 
			print 'WRONG'
			dead()
	else:
		print "You know what that was wrong?"
		dead()
start()