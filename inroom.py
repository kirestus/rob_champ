#this script will load a room from a text file and parse the valuble data for the engine


def GetRoomId(line):
	return (line)
	
def GetRoomName(line):
	return (line)
	
def GetInstanceName(line):
	return (line)
	
def GetLookList(line):
	return (line)

def GetUseList(line):
	return (line)
	
def GetTalkList(line):
	return (line)
	
def GetExitList(line):
	return (line)
	

def LoadRoom(filename, roomid):
	txt = open(filename)
	for line in txt:
		if 'room_id' in line:
			print GetRoomId(line)
		elif 'room_name' in line:
			print GetRoomName(line)
		elif 'instance_name' in line:
			print GetInstanceName(line)
		elif 'looklist' in (line):
			print GetLookList(line)
		elif 'uselist' in (line):
			print GetUseList(line)
		elif 'talklist' in (line):
			print GetTalkList(line)
		elif 'exits' in (line):
			print GetExitList(line)
	
LoadRoom('assets/room/01.txt', 01)


