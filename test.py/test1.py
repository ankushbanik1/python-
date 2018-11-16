class human:
	def __init__(self):
		self.name='ankush'
		self.head=self.HEAD()

	def display(self):
	    print('name:',self.name)
	    self.head.talk()
	    self.head.brain.think()


	class HEAD:
	    def __init__(self):
	        self.brain=self.BRAIN()


	    def talk(self):
	    	print('bok bok bok........')


	    class BRAIN:
	       def think(self):
	    	   print('THINKING,,,,,,,,,,,,,,,')


h=human()
h.display()

	            		        		        		        	