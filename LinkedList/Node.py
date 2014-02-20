class Node(object) :

	def __init__(self, value) :
		self._nextNode = None
		self._value = value

	def setNextNode(self, nextNode) :
		self._nextNode = nextNode

	def getNextNode(self) :
		return self._nextNode

	def getValue(self) :
		return self._value
