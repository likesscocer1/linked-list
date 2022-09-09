

class First_node:
	def __init__(self, data = None):
		self.data = data
		self.next = None


class Linked_list:
	def __init__(self):
		self.head = First_node()


	def add_element(self, data):
		new_node = First_node(data)
		currently_node = self.head

		while currently_node.next != None:
			currently_node = currently_node.next

		currently_node.next = new_node


	def remove(self, value):
		currently_node = self.head

		while True:
			last_node = currently_node
			currently_node = currently_node.next

			if currently_node.data == value:
				last_node.next = currently_node.next
				break
			


	def print_values(self):
		values = []
		node = self.head

		while node.next != None:
			node = node.next
			values.append(node.data)

		print(values)



my_list = Linked_list()

for number in range(1,9+1):
	my_list.add_element(number)


my_list.print_values()
my_list.remove(6)
my_list.print_values()