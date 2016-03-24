class HashTable(object):

	def __init__(self,size):
		self.size = size
		self.slots = [None] * self.size
		self.data = [None] * self.size

	def put(self,key,data):
		"""
		Hash the key by getting remainder of key and length of slots
		(key modulo size of slots list). If slots[hashvalue] == None
		then assign slots[hashvalue] = key and data[hashvalue] = data
		but if it's not empty or None, then do the following:

			if slots[hashvalue] == key (equal to given key):
				just assign given data to data[hashvalue]
				ir data[hashvalue] = data
			else if slots[hashvalue] not equal to key
			or different key with same hash value,
				We then use self.rehash(hashvalue,len(slots))
			if the rehash value is still not None under slots,
			and slots[rehash] not equal to given key
				--> We would continuously rehash the rehashed value
				until slots[rehashed] is not None and not equal to key

			Finally, if slots[rehashed] == None, then 
				slots[rehashed] = key
				data[rehashed] = data
			Else
				data[rehashed] = data
		"""
		hashvalue = self.hashfunction(key,len(self.slots))

		if self.slots[hashvalue] == None:
			self.slots[hashvalue] = key
			self.data[hashvalue] = data
		else:

			if self.slots[hashvalue] == key:
				self.data[hashvalue] = data
			else:
				if self.slots[hashvalue] == key:
					self.data[hashvalue] = data
				else:
					nextslot = self.rehash(hashvalue,len(self.slots))

					while self.slots[nextslot] != None and self.slots[nextslot] != key:
						nextslot = self.rehash(nextslot,len(self.slots))

					if self.slots[nextslot] == None:
						self.slots[nextslot] = key
						self.data[nextslot] = data
					else: self.data[nextslot] = data

	def hashfunction(self,key,size):
		return key % size

	def rehash(self, oldhash, size):
		return (oldhash + 1) % size

	def get(self, key):
		"""
		hash the given key, and check if the
		result is in slots through slots[hashvalue]

		if the slots[hash] is equal to key
		they return the value
		else continuosly rehash the given initial hashed value
		until we get the key to return the data
		else, we didn't find the data if we get back to the 
		first hash value
		"""
		startslot = self.hashfunction(key, len(self.slots))
		data = None
		stop = False
		found = False
		position = startslot

		while self.slots[position] != None and not stop and not found:
			if self.slots[position] == key:
				found = True
				data = self.data[position]
			else:
				position = self.rehash(position,len(self.slots))
				if position == startslot: #Eventually after several modulo, position would again be equal to startslot
					stop = True #This means no element was found
		return data