from sys import exit

prompt = "> "

def gold_room():
    print "In this room you see 100 gold coins on the table and another person.\nAfter short negotiations u decide to split money between you and him.\nAnyway what will be your decision - how much will you take?"

    choice = raw_input("> ")
	
    if choice.isdigit():
        how_much = int(choice)
    else:
        dead("Man, learn to use digits.")

    if how_much < 51:
        winner("Nice, you're not greedy.\nafter leaving this room with 50 gold, you finally find your horse, so you decide to leave this mad place as short as you can!")
        
    else:
        dead("You greedy bastard! - said a person after stabbing your neck with a knife.\nDiplomacy never was your best skill.\nYou are lying on the floor coughing with your own blood.")

		
	
	
def bear_room():
	print "There is a bear here."
	print "The bar has a bunch of honey."
	print "The fat bear is in front of another door."
	print "You can either try TAUNT BEAR or TAKE HONEY?"
	bear_moved = False
	
	while True:
		choice = raw_input(prompt)
		
		if choice == "take honey":
			dead("The bear looked at you then slaps your face off.")
		elif choice == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. \nYou can go through it now.\nOPEN DOOR, or maybe try to TAUNT BEAR again?"
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			dead("ROOOOOOOOOOOOOOOOOOOOAR\n(The bear gets pissed off and chews your leg off).")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."
			
			
def ctulhu_room():
	print "Here you see the great evil Ctulhu."
	print "He... or it? whatever - Ctulhu stares at you while you are going insane."
	print "Do you want to FLEE for your life or let him to eat your HEAD?"
	
	choice = raw_input(prompt)
	
	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well that was tasty! The ancient God of Depth consume u almost without pain.\nCtulhu is pleased with your offering.")
	else:
		ctulhu_room()
		

def dead(why): #this function leave game when end condition is done
	print why, "\nGood job, you are dead.\npress enter to quit." # and print this message in case of lose
	boot = raw_input()
	exit(0)

	
def winner(win):
	print win, "\nA WINNER IS YOU\npress enter to quit." # and print this message in case of win
	winno = raw_input()
	exit(0)

def start():
	print "You are in a dark room."
	print "There is a door: to the RIGHT and to the LEFT."
	print "Which one do you take?"
	
	choice = raw_input(prompt)
	
	if choice == "left":
		bear_room()
	elif choice == "right":
		ctulhu_room()
	else:
		dead("You stumble around the room until you starve.")
		
		
start()