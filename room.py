class Room(object):

    #This initiates the class taking the number sent and filling in the blanks
	def __init__(self, num,state):	
		self.SetRoom(num, state)
		
	#Define rooms in here
	def SetRoom(self,number,state):
		
		#Room 1 confrence hall
		if number == 1:
			self._roomName = "The Hotel Room"
			self._roomIntro = (
			"The first thing you are aware of before you even open your eyes is an intense ringing in \n"
			"your head. You bring your hands to your ears to try to block out the sound, but it does \n"
			"no good. Your hands come away sticky, presumably with blood. You smell smoke. You have no \n"
			"idea of your surroundings and no memory of how you got here. \n" 
			"\nWhat do you do?")
			self._roomDesc = (
			"You are in what appears to be a hotel room. It's nice, or would be without the scorch marks\n"
			"all over the walls and broken glass littering the floors from the shattered windows and \n"
			"mirrors. The bed is made up, but slightly disheveled - almost as if someone lay down on top\n"
			"to discretely have a nap. The door to the hotel room has been splintered. It looks as if the\n"
			"digital card lock has exploded"
			)
			self._options = options = ['N','S']
			self._ifNorth = "You Proceed through an open door to the north"
			self._ifSouth = "You try the door to the south but it is locked"
			self._lookList = ['Hands','']

		#ROOM 2 the Long Hallway
		if number == 2:
			self._roomName = "Long Hallway"
			self._roomDesc = ("A long boring hallway"
			"\nThere are exits to the East and South")
			self._options = options = ['E','S']
			
		return number
	
	def PrintIntro(self):
		print self._roomIntro
			
	def PrintRoom(self):
		print "%s:"%self._roomName
		print self._roomDesc		
			
	
	def GoTo(self, num):
		pdir = self._options
		print "possible options %r" %pdir
		choice = raw_input("Go Where? N,E,S,W >")
		for direction in pdir:
			if direction == choice:
				if direction == "N":
					print self._ifNorth
				elif direction == "E":
					print self._ifEast
				elif direction == "S":
					print self._ifSouth
				elif direction == "W":
					print self._ifWest
				return 1
		print "There is no %s exit"%choice
		return 0
