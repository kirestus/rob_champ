
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
sceneNum = 01
stateNum = 01
#create a room named hotelroom and set the state of it to room 01 state 01
room_hotelroom = room.Room(sceneNum,stateNum)
room_hallway = room.Room(02,01)
#updates the list of people whom the player may speak with in the TalkTo script
talkto = TalkTo.TalkTo(sceneNum)
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
	print "/////////////////////" 
	

def SetRoom(number):
	if number == 1:
		return room_hotelroom
	if number == 2:
		return room_hallway
		
#current room set
current_room = SetRoom(1)		
current_room.PrintIntro()

#mainloop the game runs in	
while rungame == 1:
	#update room may change out in favor of literally creating new rooms with classes
	room_hotelroom.SetRoom(sceneNum, stateNum)
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
		if room_confhall.GoTo(sceneNum) == 1:
			sceneNum += 1;
			print sceneNum
	elif choice == '6':
		addItem = raw_input ("What do you want to pick up?> ")
		player.AddItem(addItem)
	elif choice == '7':
		player.ListItems()
	else:
		rungame = 0
	raw_input ("Press [ENTER] to continue")
	sysclear()	
