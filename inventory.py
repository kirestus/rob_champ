class Inventory(object):
	
	def __init__(self):	
		self._itemlist = []
		
	#add an item that has name	
	def AddItem(self, name):
		self._itemlist.append(name)
	
	#List all of the items 	
	def ListItems(self):
		#If inventory is empty then print Empty
		if len(self._itemlist) == 0:
			print "Empty"
		#else print out list one item at a time
		else:
			for item in self._itemlist:
				print item
	
	#check to see if player has reqested item in their possesion 	
	def HaveItem(self, haveitem):
		for item in self._itemlist:
			if item == haveitem:
				return 1
		print "You dont have %s in your inventory"% haveitem
		
	def UseItem(self):
		item = raw_input("What item do you want to use?> ")
		if self.HaveItem(item) == 1:
			self.RemoveItem(item)
			print "great JORB!!"
			return 1
		else:
			return 0
	
	def RemoveItem(self, name):
		if name in self._itemlist:
			self._itemlist.remove(name)
