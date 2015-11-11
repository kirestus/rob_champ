import inroom
import textwrap
class Room(object):

    #This initiates the class taking the number sent and filling in the blanks
	def __init__(self, num,state):	
		self.SetRoom(num, state)
		
	#Define rooms in here
	def SetRoom(self,number,state):
		
		#Room 1 confrence hall
		if number == 1:
			roomtxt = 'assets/room/01.txt'
			self._roomName = inroom.LoadRoom(roomtxt, number, 'room_name')
			self._roomIntro = inroom.LoadRoom('assets/room/01.txt', number, 'room_intro')
			self._roomDesc = inroom.LoadRoom('assets/room/01.txt', number, 'room_desc')
			self._options = options = ['N']
			self._ifNorth = "You Proceed through an open door to the north"
			self._lookList = inroom.LoadRoom('assets/room/01.txt', number,'looklist')
			self._pickupList = inroom.LoadRoom('assets/room/01.txt', number,'pickuplist')
			self._useList = inroom.LoadRoom('assets/room/01.txt', number,'uselist')
			self._talkList = inroom.LoadRoom('assets/room/01.txt', number,'talklist')





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
		print textwrap.fill(self._roomIntro,100)
			
	def PrintRoom(self):
		print textwrap.fill(self._roomDesc,100)	
		
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
