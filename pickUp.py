#this module contains the code needed to input what your character is looking at

#this is called from the engine.py script and will pass the variables to the other functions
def PickupInit(pickupList,sceneNum):
	pickupwhat = raw_input("what do you want to pick up?> ")
	pickupwhat = pickupwhat.lower()
	if PickUpList(pickupList,pickupwhat) == True:
		#this returns the item that is being picked up to the main loop
		return (PrintItemLook(pickupwhat, sceneNum))
	

#this will check the list of variables and see if it works
def PickUpList(pickuplist, pickupwhat):
	for item in pickuplist:
		if item == pickupwhat:
			return (True)
	print "You can't pick up anything that matches the description %s"% pickupwhat
	print pickuplist
	

#this will tell set the variable pickupDesc to return the item being picked up
def PrintItemLook(pickupwhat, sceneNum):
	if sceneNum == 1:
		if pickupwhat == "ticket":
			print "check your inventory jackass"
			return (pickupwhat)
		
		elif pickupwhat == "glass":
			print "No. That looks sharp"
	
	return ("nul")