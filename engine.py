import room
import inroom
import lookAt
import pickUp
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
#create an entity of all the specific rooms that we will be needing setting their state and number
room_hotelroom = room.Room(_sceneNum,_stateNum)
room_hallway = room.Room(02,01)
room_ballroom = room.Room(03,01)
room_restaurant = room.Room(04,01)
room_parkade = room.Room(05,01)
room_lobby = room.Room(06,01)
room_street = room.Room(07,01)
room_goreindustries = room.Room(20,01)


#updates the list of people whom the player may speak with in the TalkTo script
talkto = TalkTo.TalkTo(_sceneNum)
#creates an inventory for the player named player and adds the items cookbook and party hat
player = inventory.Inventory()
player.AddItem("Party Hat")
player.AddItem("Cookbook")

sysclear()
rungame =1;

#make the computer beep 
def Beep(number):
	if number == 1:
		Freq = 250 # Set Frequency To 2500 Hertz
		Dur = 150 # Set Duration To 1000 ms == 1 second
	elif number == 2:
		Freq = 150 # Set Frequency To 2500 Hertz
		Dur = 150 # Set Duration To 1000 ms == 1 second
	winsound.Beep(Freq,Dur)

#this function will draw the menu for the user	
def DrawMenu():
	str1 = "/////////////////////"
	str2 = "// 1.) Look Around //"
	str3 = "// 2.) Look At     //"
	str4 = "// 3.) Use         //"
	str5 = "// 4.) Talk to     //"
	str6 = "// 5.) Go to       //"
	str7 = "// 6.) Pick Up     //"
	str8 = "// 7.) Inventory   //"
	str9 = "// 8.) Use Item    //"
	str10= "// 0.) Exit        //"
	str11= "/////////////////////"
	strlist = [str1,str2,str3,str4,str5,str6,str7,str8,str9,str10,str11]
	#print all the rows in the center or wherever we decide to put them
	for i in strlist:
		print i
	#Beep(1)
	
#this function simply returns the propper room depending on the number it is fed
def SetRoom(number):
	if number == 1 or number == "hotel":
		return room_hotelroom
	if number == 2 or number == "hallway":
		return room_hallway
		
#current room set
current_room = SetRoom(1)		


#overly complex solution to changing the rooms in the engine
def ChangeRoom(_sceneNum,current_room):
	#This is where it gets complicated in trying to show what rooms you can travel to from what 
	#if in hotel room
	goto = current_room.GoTo(_sceneNum)
	if goto == 1 and current_room == SetRoom('hotel'):
		current_room = SetRoom(2)
		_sceneNum = 2
	elif goto == 3 and current_room == SetRoom('hallway'):
		current_room = SetRoom(1)
		_sceneNum = 1
	return (current_room, _sceneNum)


#mainloop the game runs in	
while rungame == 1:
	current_room = SetRoom(_sceneNum)
	#update room may change out in favor of literally creating new rooms with classes
	current_room.SetRoom(_sceneNum, _stateNum)
	current_room.PrintIntro()
	DrawMenu()
	choice = raw_input ("> ")
	choice = choice.upper()
	
	#if you choose 1 this will print the room info out
	if (choice == '1') or (choice == 'LOOK AROUND'):
		current_room.PrintRoom()
	
	#if you choose 2 this will call the LookInit fucntion from the lookAt module sending the looklist from the correct scene 
	elif (choice == '2') or (choice == 'LOOK AT'):
		lookAt.LookInit(current_room.GetLookList(),_sceneNum)
	
	#if you choose 3 this will use items in the environment
	elif (choice == '3') or (choice == 'USE'):
		print "coming soon"
	
	#if you choose 4 then you will talk to who you enter as a raw input. ///note[this doesnt need to be a class]
	elif (choice == '4') or (choice == 'TALK TO'):
		whom = raw_input("Talk to whom?> ")
		talkto.TalkToWhom(whom)
	
	#if you choose 5 things get a bit more tricky, ill have to see what i did later
	elif (choice == '5') or (choice == 'GO TO') or (choice =='GO'):
		roomvars = current_room = ChangeRoom(_sceneNum,current_room)
		current_room = roomvars[0]
		_sceneNum = roomvars[1]
	
	#the player can add an item to his inventory using this function
	elif (choice == '6')or (choice == "PICKUP") or (choice== 'PICK UP'):
		player.AddItem(pickUp.PickupInit(current_room.GetPickUpList(),_sceneNum))
	
	#if player chooses 7 then you can go through a list of items in the player inventory
	elif (choice == '7')or(choice == 'INVENTORY')or (choice == 'ITEMS'):
		player.ListItems()
	
	#if you choose 8 the run the UseItem function in the inventory class
	elif (choice == '8')or(choice == 'USE ITEM'):
		player.UseItem()
	
	#if you choose 8 the run the UseItem function in the inventory class
	elif (choice == '666')or(choice == 'Hail Satan'):
		print "Satan Devours your soul"
		rungame = 0
	
	#if player chooses 0 then stop the game loop causing the program to end
	elif (choice == '0')or (choice == "EXIT"):
		rungame = 0
	print 
	raw_input ("Press [ENTER] to continue")
	sysclear()
	
	
	

