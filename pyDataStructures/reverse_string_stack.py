from stack import Stack

input_str = 'Hello'

def reverse_string(stack, input_str):

	for i in input_str:
		stack.push(i)

	rev_str = ''
	while not stack.is_empty():
		rev_str += stack.pop()

	return rev_str

stack = Stack()

print(reverse_string(stack, input_str))

print(input_str[::-1])