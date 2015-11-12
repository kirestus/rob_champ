from xml.etree import ElementTree
import textwrap
#this module contains the code needed to input what your character is looking at by taking the list of possible things he may look at and the scene number and returns the description

#this is called from the engine.py script and will pass the looklist and scenenum to the other functions in the module
def LookInit(looklist,sceneNum):
	lookatwhat = raw_input("what do you want to look at?> ")
	lookatwhat = lookatwhat.lower()
	#if the item you want to look at is indeed in the room you are in this fucntion will print it's description out
	if LookAtList(looklist,lookatwhat) == True:
		lookatthis = PrintItemLook(lookatwhat, sceneNum)
		print textwrap.fill(lookatthis,100)
	
	

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
	if sceneNum == 01:
		filename = 'assets/room/01.xml'
	elif sceneNum == 02:
		filename = 'assets/room/02.xml'
	with open(filename, 'r') as f:
		tree = ElementTree.parse(f)
		for node in tree.iter('item'):
			if node.attrib.get('name') == lookatwhat:
				result = node.attrib.get('lookdesc')
		return(result)
	return("nope")