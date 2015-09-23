class TalkTo(object):
	
	def __init__(self,num):
		self._scene = num
		if num == 00:
			self._list = ["Credits"]
		if num == 01:
			self._list = ["GodMode","Rob"]
		
	def TalkToWhom(self, person):
		for personx in self._list:
			if person == personx:
				print 'You say "sup" to %s' %person
				self.Respond(person)
				return 1
		print "%s Is not here"%person
		
	def Respond(self, person):
		if person == "Credits":
			print"Engine By John Ryan Fry, Game Design by Matt Root"
		if self._scene == 01 and person == "Rob":
			print '"... I dont want to talk to myself right now"'
		if self._scene == 01 and person == "GodMode":
			print"no cheating!"
	
