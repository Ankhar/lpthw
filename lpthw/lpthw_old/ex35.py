from sys import exit

prompt = "> "

def gold_room():
    print "This room is full of gold.  How much do you take?"

    choice = raw_input("> ")
	
    if choice.isdigit():
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")

		
	
	
def bear_room():
	print "There is a bear here."
	print "The bar has a bunch of honey."
	print "The fat bear is in front of another door."
	print "You can either try taunt bear or take honey?"
	bear_moved = False
	
	while True:
		choice = raw_input(prompt)
		
		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif choice == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now. Type 'open door' ...to open door"
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."
			
			
def ctulhu_room():
	print "Here you see the great evil Ctulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"
	
	choice = raw_input(prompt)
	
	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well that was tasty!")
	else:
		ctulhu_room()
		

def dead(why): #this function leave game when end condition is done
	print why, "Good job!" # and print this message in any case
	exit(0)

def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"
	
	choice = raw_input(prompt)
	
	if choice == "left":
		bear_room()
	elif choice == "right":
		ctulhu_room()
	else:
		dead("You stumble around the room until you starve.")
		
		
start()