class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None
										
	def print_list(self):
		cur_node = self.head
		while cur_node:
			print(cur_node.data)
			cur_node = cur_node.next

	def append(self, data):
		new_node = Node(data)

		if self.head is None:
			self.head = new_node
			return

		last_node = self.head
		while last_node.next:
			last_node = last_node.next
		last_node.next = new_node

	def prepend(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def insert_after_node(self, prev_node, data):

		if not prev_node:
			print('previous node not present')
			return

		new_node = Node(data)

		new_node.next = prev_node.next
		prev_node.next = new_node

	def delete_node(self, key):

		cur_node = self.head
		if cur_node and cur_node.data == key:
			self.head = cur_node.next
			cur_node = None
			return 

		prev = None
		while cur_node and cur_node.data != key:
			prev = cur_node
			cur_node = cur_node.next

		if cur_node is None:
			return
		prev.next = cur_node.next
		cur_node = None

	def delete_node_at_pos(self, pos):
		cur_node = self.head

		if pos == 0:
			self.head = cur_node.next
			cur_node = None
			return 

		prev = None
		count = 0
		while cur_node and count != pos:
			prev = cur_node
			cur_node = cur_node.next
			count += 1

		if cur_node is None:
		 	return

		prev.next = cur_node.next
		cur_node = None

	def len_iterative(self):
		cur_node = self.head
		count = 0
		while cur_node:
			count += 1
			cur_node = cur_node.next
		return count

	def len_recursive(self, node):
		if node is None:
			return 0
		return 1 + self.len_recursive(node.next)

	def swap_nodes(self, key_1, key_2):
		if key_1 == key_2:
			return

		prev_1 = None
		curr_1 = self.head
		while curr_1 and curr_1.data != key_1:
			prev_1 = curr_1
			curr_1 = curr_1.next

		prev_2 = None
		curr_2 = self.head
		while curr_2 and curr_2.data != key_2:
			prev_2 = curr_2
			curr_2 = curr_2.next

		if not curr_1 or not curr_2:
			return 	

		if prev_1:
			prev_1.next = curr_2
		else:
			self.head = curr_2

		if prev_2:
			prev_2.next = curr_1
		else:
			self.head = curr_1

		curr_1.next, curr_2.next = curr_2.next, curr_1.next	

	def print_helper(self, node, name):
		if node is None:
			print(node + ': None')
		else:
			print(name + ':' + node.data)

	def reverse_iterative(self):

		prev = None
		curr_node = self.head
		while curr_node:
			nxt = curr_node.next
			curr_node.next = prev

			# self.print_helper(prev, 'PREV')
			# self.print_helper(cur_node, 'CURR_NODE')
			# self.print_helper(nxt, 'NXT')

			prev = curr_node
			curr_node = nxt
			
		self.head = prev

	def merge_sorted(self, llist):

		p = self.head
		q = llist.head
		s = None

		if not p:
			return q
		if not q:
			return p

		if p and q:
			if p.data <= q.data:
				s = p
				p = s.next
			else:
				s = q
				q = s.next
			new_head = s

		while p and q:
			if p.data <= q.data:
				s.next = p
				s = p 
				p = s.next
			else:
				s.next = q
				s = q
				q = s.next

		if not p:
			s.next = q
		if not q:
			s.next = p
		
		return new_head

	def remove_duplicates(self):

		cur_node = self.head
		prev = None
		dup_values = dict()

		while cur_node:
			if cur_node.data in dup_values:
				prev.next = cur_node.next
				cur_node = None
			else:
				dup_values[cur_node.data] = 1
				prev = cur_node

			cur_node = prev.next

	def print_nth_from_last(self, n):

		# method 1:
		total_len = self.len_iterative()

		cur = self.head
		while cur:
			if total_len == n:
				print(cur.data)
				return cur
			total_len -= 1
			cur = cur.next
		if cur is None:
			return

	def print_nth_from_last_method2(self, n):
		p = self.head
		q = self.head
		count = 0
		while q and count < n:
			q = q.next
			count += 1
		if not q:
			print(str(n) + ' is greater than the number of nodes in the list')
			return 
		while p and q:
			p = p.next
			q = q.next
		return p.data

llist_1 = LinkedList()
llist_2 = LinkedList()

llist_1.append('A')
llist_1.append('B')
llist_1.append('C')
llist_1.append('D')

# llist_2.append(2)
# llist_2.append(3)
# llist_2.append(4)
# llist_2.append(6)
# llist_2.append(8)

# llist_1.delete_node_at_pos(1)

# llist_1.insert_after_node(llist_1.head.next, 'E')

# print(llist_1.len_iterative())

# print(llist_1.len_recursive(llist_1.head))

# llist_1.swap_nodes('A', 'B')

# llist_1.reverse_iterative()

# llist_1.merge_sorted(llist_2)

# llist_1.remove_duplicates()

# llist_1.print_nth_from_last(2)

# print(llist_1.print_nth_from_last_method2(2))

llist_1.print_list()




 
 
	





