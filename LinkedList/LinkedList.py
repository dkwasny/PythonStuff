from Node import Node

class LinkedList(object) :
	def __init__(self) :
		self._startNode = None
		self._endNode = None

	def append(self, value) :
		newNode = Node(value)
		if self._startNode == None :
			self._startNode = newNode
		
		if self._endNode != None :
			self._endNode.setNextNode(newNode)
		
		self._endNode = newNode

	def get(self, index) :
		currNode = self._startNode
		count = 0;

		while count < index :
			if currNode == None :
				print "You dun goofed!"
				exit()
			currNode = currNode.getNextNode()
			count += 1

		return currNode.getValue()
