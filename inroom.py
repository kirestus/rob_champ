from xml.etree import ElementTree


def LoadRoom(filename, roomid, query):
#	open the filename you passed when calling the function
	with open(filename, 'r') as f:
		tree = ElementTree.parse(f)
		#if the query is for a room atribute such as name
		if query == 'room_name' or query == 'room_id' or query == 'room_id' or query == 'room_desc' or query == 'room_intro' or query == 'room_exits':
			for node in tree.iter('room'):
				result = node.attrib.get(query)
				return(result)
			return ('failstate')
		#else if the query is for a room item object
		elif query == 'looklist' or query == 'uselist' or query == 'pickuplist':
			result = []
			for node in tree.iter('item'):
				querytrue = node.attrib.get(query)
				if querytrue =='y':
					result.append(node.attrib.get('name'))
			return(result)
		#this will search the xml file for the room exits and return them
		elif query == 'room_exits':
			for node in tree.iter('room'):
				exits = node.attrib.get('exits')
				return(exits)
		#this will return the text blurb you get for going north east south or west
		elif query == 'room_ifnorth' or query == 'room_ifeast' or query == 'room_ifsouth' or query == 'room_ifwest':
			for node in tree.iter('room'):
				exits = node.attrib.get(query)
				return(exits)
		#return if failed
		else:
			return("not a valid query")
