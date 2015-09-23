class Room(object):

    #This initiates the class taking the number sent and filling in the blanks
	def __init__(self, num,state):	
		self.SetRoom(num, state)
		
	#Define rooms in here
	def SetRoom(self,number,state):
		
		#Room 1 confrence hall
		if number == 1:
			self._roomName = "Conference Hall"
			self._roomDesc = ("You Find yourself in a ball room with nothing but a Bobby Flay"
			" Cook Book and a Y2K party hat"
			"\nThere are exits to the North and South")
			self._options = options = ['N','S']
			self._ifNorth = "You Proceed through an open door to the north"
			self._ifSouth = "You try the door to the south but it is locked"

		#ROOM 2 the Long Hallway
		if number == 2:
			self._roomName = "Long Hallway"
			self._roomDesc = ("A long boring hallway"
			"\nThere are exits to the East and South")
			self._options = options = ['E','S']
			
		return number
			
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
