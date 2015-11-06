#this module contains the code needed to input what your character is looking at by taking the list of possible things he may look at and the scene number and returns the description

#this is called from the engine.py script and will pass the looklist and scenenum to the other functions in the module
def LookInit(looklist,sceneNum):
	lookatwhat = raw_input("what do you want to look at?> ")
	lookatwhat = lookatwhat.lower()
	#if the item you want to look at is indeed in the room you are in this fucntion will print it's description out
	if LookAtList(looklist,lookatwhat) == True:
		print PrintItemLook(lookatwhat, sceneNum)
	
	

#this will check the list of variables and see if it works
def LookAtList(looklist, lookatwhat):
	for item in looklist:
			if item == lookatwhat:
				return (True)
	#if not true print this 
	print "You dont see anything that matches the description %s"% lookatwhat
	#this is included for tesing and debug will be removed at later date
	print looklist
	

#this will tell set the variable itemDesc to the propper items description
def PrintItemLook(lookatwhat, sceneNum):
	if sceneNum == 1:
		if lookatwhat == "hands":
			itemDesc = ("Yep. That's blood. That's probably not good.\n"
			"You notice that you are wearing a broken mechanical watch.\n" 
			"The display still reads the exact time and date that it stopped: 12:00.\n"
			"You are also wearing a diamond encrusted ring on your left ring finger.")
		elif (lookatwhat == "windows") or (lookatwhat == "window"):
			itemDesc = ("In the early dawn light you see the silhouettes of many skyscrapers.\n"
			"You can tell by the distinctive shape of the World Trade Center twin towers that you are in New York City.\n"
			"All the lights are out in the city.\n"
			"Judging from the colour of the sky, there would be a beautiful sunrise to look at if there weren't a huge black building in the way")
		elif lookatwhat == "black building":
			itemDesc = ("A giant black monolith. You can see the Gore Industries logo on the side.\n"
			"These are the people who make the internet.")
		elif lookatwhat == ("world trade center") or (lookatwhat == "twin towers"):
			itemDesc = "Built to last"
			
		elif lookatwhat == "mirrors":
			itemDesc = "These are totally smashed"
		
		elif (lookatwhat == "digital card lock") or (lookatwhat == "card lock"):
			itemDesc = "There are only tiny bits of shrapnel remaining embedded in the walls."
		
		elif lookatwhat == "door":
			itemDesc = "There really isn't much left"
		
		elif lookatwhat == "glass":
			itemDesc = ("In a large fragment of broken mirror, you catch your reflection.\n"
			"A bed-headed young man in a rumpled dinner jacket.\n"
			"There is unmistakably some lipstick on your shirt collar and crusty drool on your face. ")	
		elif lookatwhat == "bed":
			itemDesc = ("Looking closer at the bed, you notice that there is a small slip of paper in the blankets.\n"
			"It appears to be a coat check ticket")	
		elif lookatwhat == "ticket":
			itemDesc = "Number 408"
	
	if sceneNum == 2:
		if lookatwhat == "body":
			itemDesc = ("It appears to be a hotel employee, possibly a housekeeper or waiter, judging by the uniform.\n"
			"The individual's head has been turned into a bloody pulp... gross!\n"
			"A narrow cable extends from the uniform pocket and lies severed alongside the body.")
		elif lookatwhat == "housekeeping cart":
			itemDesc = "The cart contain various towels."
		elif lookatwhat == "towels":
			itemDesc = "Clean and fluffy. You wonder how many people's' butts these things have touched."
		elif lookatwhat == "uniform":
			itemDesc = "It's a polyester number in robin's-egg blue."
		elif lookatwhat == "cable":
			itemDesc = "Upon further inspection, the cable seems to be coming from a Sony discman."
		elif lookatwhat == "discman":
			itemDesc = ("Pretty cool. Too bad it looks like the headphones exploded... \n"
			"It makes you think of a personal Manowar concert for one.")
		elif lookatwhat == "elevator":
			itemDesc = ('unlike most of the electronics you have encountered, the elevator control panel seems to be in fine working order.\n'
			'There is an up button and a down button.')
			

	return (itemDesc)
