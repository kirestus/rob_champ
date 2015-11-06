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
			self._options = options = ['N']
			self._ifNorth = "You Proceed through an open door to the north"
			self._lookList = ['hands','surroundings','windows','window','black building','world trade center','twin towers','mirrors','digital card lock','card lock','door','glass','bed','ticket']
			self._pickupList = ['ticket','glass']
			self._useList = ['bed','door']
			self._talkList = ["godMode","rob"]





		#ROOM 2 the hallway
		if number == 2:
			self._roomName = "The Hallway"
			self._roomIntro = (
			"The doors to all the other rooms on the floor have suffered the same fate as the one you just\n"
			"passed through. At one end of the hallway is an elevator and a stairwell, at the other there\n"
			"appears to be a body."
			)
			self._roomDesc = (
			"The doors to all the other rooms on the floor have suffered the same fate as the one you just\n"
			"passed through. At one end of the hallway is an elevator and a stairwell, at the other there\n"
			"appears to be a body."
			
			"\nThere are exits to the South")
			self._options = options = ['S']
			self._ifSouth = "You Proceed South back to the Hotel Room"
			self._lookList = ['body','cable','discman','elevator']
			self._pickupList = ['uniform','body','discman']
			self._useList = ['discman','elevator','elevator car','']
			
		return number
	
	def PrintIntro(self):
		print "%s:"%self._roomName
		print self._roomIntro
			
	def PrintRoom(self):
		print self._roomDesc	
		
	def GetLookList(self):
		return self._lookList	
	
	def GetPickUpList(self):
		return self._pickupList
			
	
	def GoTo(self, num):
		pdir = self._options
		print "possible options %r" %pdir
		choice = raw_input("Go Where? N,E,S,W > ")
		for direction in pdir:
			if direction == choice:
				if direction == "N":
					print self._ifNorth
					return 1
				elif direction == "E":
					print self._ifEast
					return 2
				elif direction == "S":
					print self._ifSouth
					return 3
				elif direction == "W":
					print self._ifWest
					return 4
		print "There is no %s exit"%choice
		return 0
