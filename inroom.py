#this script will load a room from a text file and parse the valuble data for the engine
def LoadRoom(filename, roomid):
	txt = open(filename)
	line = txt.readline()
	
	print "here it is ryan"
	while line:
		
	
		print line
		line =txt.readline()
	
LoadRoom('assets/room/01.txt', 01)
