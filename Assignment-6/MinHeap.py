class minheap(object):
	__slots__ = ['_size','_array']

	def __init__(self,firstOb):
		self._size = 0
		self._array = [firstOb]
		for i in range(100):
			self._array.append(firstOb)
	
	def __len__(self):
		return self._size

	def display(self):
		i = 1
		while i <= self._size:
			print(str(self._array[i]))
			i = i + 1

	def insert(self,newOb):
		self._size = self._size + 1
		i = self._size
		
		while self._array[i//2] > newOb:
			self._array[i] = self._array[i//2]
			i = i // 2
	
		self._array[i] = newOb
	
	def delete(self):
		if self._size == 0:
			return None
		
		min = self._array[1]
		last = self._array[self._size]
		self._size = self._size - 1

		i = 1
		while i * 2 <= self._size:
			child = i * 2
		
			if child != self._size and self._array[child + 1] < self._array[child]:
				child += 1
			
			if last > self._array[child]:
				self._array[i] = self._array[child]
			else:
				break
			
			i = child

		self._array[i] = last
		return min

		
	
