from sys import exit

def gold_root():
	print "THis room is full of gold. How much do you take?"
	
	choice = raw_input("> ")
	if "0" in choice or "1" in choice:
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
	print "THe bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False
	
	while True:
		choice = raw_input("> ")
		
		if choice == "take honey":
			dead("THe bear looks at you then slaps your face off.")
		elif choice == "Taunt bear" and not bear_moved:
			print "THe bear has moved from the door. You can go through it now."
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idead what that means."
			
def dead(why):
	print why, "Good job!"
	exit(0)
	
def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "which one do you take?"
	
	choice = raw_input("> ")
	
	if choice == "left":
		bear_room()
	elif choice == "right":
		print "add this"
	else:
		dead("You stumble around the room until you starve.")
		
start()