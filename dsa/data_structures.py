# Linked List
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def insertAtBegin(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def insertAtIndex(self, data, index):
		if index == 0:
			self.insertAtBegin(data)
			return

		# start from 1st node and keep shifting till next node is in target index
		position = 0
		current_node = self.head
		while current_node is not None and position + 1 != index:
			position += 1
			current_node = current_node.next

		# insert new node in front of current node
		if current_node is not None:
			new_node = Node(data)
			new_node.next = current_node.next
			current_node.next = new_node

	def insertAtEnd(self, data):
		new_node = Node(data)

		# case for empty LL
		if self.head is None:
			self.head = new_node
			return

		# keep shifting till node has no next
		current_node = self.head
		while current_node.next:
			current_node = current_node.next

		current_node.next = new_node

	def updateNode(self, val, index):
		# start at head
		current_node = self.head
		position = 0
		# keep shifting till next node is at target index
		while current_node is not None and position + 1 != index:
			position += 1
			current_node = current_node.next

		if current_node is not None:
			current_node.data = val

	def removeFirstNode(self):
		# case for empty LL
		if self.head is None:
			return

		self.head = self.head.next

	def removeLastNode(self):
		# case for empty LL
		if self.head is None:
			return

		# if only 1 node
		if self.head.next is None:
			self.head = None
			return

		# shift all the way till 2nd last node
		current_node = self.head
		while current_node.next and current_node.next.next:
			current_node = current_node.next

		current_node.next = None

	def removeAtIndex(self, index):
		# case for empty LL
		if self.head is None:
			return

		if index == 0:
			self.removeFirstNode()
			return

		current_node = self.head
		position = 0
		while current_node is not None and current_node.next is not None and position + 1 != index:
			position += 1
			current_node = current_node.next

		if current_node is not None and current_node.next is not None:
			current_node.next = current_node.next.next

	def removeNodeByData(self, data):
		current_node = self.head

		# if node to be removed is head
		if current_node is not None and current_node.data == data:
			self.removeFirstNode()
			return

		# starting from head, traverse and find node with matching data
		while current_node is not None and current_node.next is not None:
			# if next node is the one to be removed
			if current_node.next.data == data:
				current_node.next = current_node.next.next
				return

			# else continue
			current_node = current_node.next

		# if data not found
		print("Node with given data not found")

	def getSize(self):
		size = 0
		current_node = self.head

		while current_node:
			size += 1
			current_node = current_node.next

		return size

	def printLL(self):
		current_node = self.head
		while current_node:
			print(current_node.data)
			current_node = current_node.next

# create a new linked list
llist = LinkedList()

# add nodes to the linked list
llist.insertAtEnd('a')
llist.insertAtEnd('b')
llist.insertAtBegin('c')
llist.insertAtEnd('d')
llist.insertAtIndex('g', 2)

# print the linked list
print("Node Data:")
llist.printLL()

# remove nodes from the linked list
print("\nRemove First Node:")
llist.removeFirstNode()
llist.printLL()

print("\nRemove Last Node:")
llist.removeLastNode()
llist.printLL()

print("\nRemove Node at Index 1:")
llist.removeAtIndex(1)
llist.printLL()

# print the linked list after all removals
print("\nLinked list after removing a node:")
llist.printLL()

print("\nUpdate node Value at Index 0:")
llist.updateNode('z', 0)
llist.printLL()

print("\nSize of linked list:", llist.getSize())

# stack
# FILO
# push
# pop
# peek
# isEmpty
# size


class Stack:
	def __init__(self, size):
		self.stack = []
		self.size = size

	def push(value):
		self.stack.append(value)

	def pop():
		if (self.stack.size == 0):
			print("Stack is empty, nothing to pop")
		else:
			self.stack.pop()

	def peek():
		if (self.stack.size == 0):
			print("Stack is empty")
		else:
			return self.stack[-1]

	def isEmpty():
		return size == 0
