#this script will load a room from a text file and parse the valuble data for the engine
	
#take the filename roomid and a search query
def LoadRoom(filename, roomid, query):
	#open the filename you passed when calling the function
	txt = open(filename)
	for line in txt:
		if query in line:
			#this splits the line after the = so that we can just take the values we need
			result = line.split('= ',1)[1]
			resultList = result.split('^')
			resultListItems = []
			for i in resultList:
				resultListItems.append(i);
			if len(resultListItems)>1:
				return resultListItems
			else:
				return result
	return ("nul")
	


