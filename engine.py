import room
import inventory
import TalkTo
import os

#clears the sceen depending on what os the user is running
def sysclear():
	if os.name == 'nt':
		return os.system("cls")
	else:
		return os.system("clear")

#Sets the current scene Number and State Number for each scene
_sceneNum = 01
_stateNum = 01
#create a room named hotelroom and set the state of it to room 01 state 01
room_hotelroom = room.Room(_sceneNum,_stateNum)
room_hallway = room.Room(02,01)
#updates the list of people whom the player may speak with in the TalkTo script
talkto = TalkTo.TalkTo(_sceneNum)
#creates an inventory for the player named player and ads the items cookbook and party hat
player = inventory.Inventory()
player.AddItem("Party Hat")
player.AddItem("Cookbook")

sysclear()
rungame =1;

#this function will draw the menu for the user	
def DrawMenu():
	print "/////////////////////"
	print "// 1.) Look Around //"
	print "// 2.) Look At     //"
	print "// 3.) Use Item    //"
	print "// 4.) Talk to     //"
	print "// 5.) Go to       //"
	print "// 6.) Pick Up     //"
	print "// 7.) Inventory   //"
	print "// 0.) Exit        //"
	print "/////////////////////" 
	

def SetRoom(number):
	if number == 1:
		return room_hotelroom
	if number == 2:
		current_room.SetRoom(_sceneNum, _stateNum)
		return room_hallway
		
#current room set
current_room = SetRoom(1)		

#mainloop the game runs in	
while rungame == 1:
	print _sceneNum
	current_room = SetRoom(_sceneNum)
	print current_room
	#update room may change out in favor of literally creating new rooms with classes
	current_room.SetRoom(_sceneNum, _stateNum)
	current_room.PrintIntro()
	DrawMenu()
	choice = raw_input ("> ")
	
	if choice == '1':
		current_room.PrintRoom()
	elif choice == '2':
		current_room.LookList()
	elif choice == '3':
		player.UseItem()
	elif choice == '4':
		whom = raw_input("Talk to whom?> ")
		talkto.TalkToWhom(whom)
	elif choice == '5':
		#if in hotel room
		goto = current_room.GoTo(_sceneNum)
		if goto == 1:
			current_room = SetRoom(2)
			_sceneNum = 2
		#elif
		elif goto == 2:
			print "BINGO!"
			current_room = SetRoom(1)
			_sceneNum = 1
	elif choice == '6':
		addItem = raw_input ("What do you want to pick up?> ")
		player.AddItem(addItem)
	elif choice == '7':
		player.ListItems()
	elif choice == '0':
		rungame = 0
	print 
	raw_input ("Press [ENTER] to continue")
	sysclear()	
