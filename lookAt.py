#this module contains the code needed to input what your character is looking at

#this will return either 
def LookAtRoom(looklist):
	lookatwhat = raw_input("what do you want to look at?> ")
	lookatwhat = lookatwhat.lower()
	for item in looklist:
			if item == lookatwhat:
				print "IT WORKS!!!!"
				return (1,lookatwhat)
	print "You dont see anything that matches the description %s"% lookatwhat
	print looklist
	

