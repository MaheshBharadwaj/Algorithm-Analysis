class tree(object):
	__slots__ = ['_left','_right','_root']

	def __init__(self):
		self._left = None
		self._right = None

	def setLeft(self,lNode):
		self._left = lNode

	def setRight(self,rNode):
		self._right = rNode
	
	def getLeft(self):
		return self._left

	def getRight(self):
		return self._right
