# calculate string length

input_str_2 = 'viratchaudhary'

def str_length_iterative(input_str):
	count = 0
	for i in input_str:
		count += 1
	return count

def str_length_recursive(input_str):
	if input_str == '':
		return 0
	return 1 + str_length_recursive(input_str[1:])

print(str_length_iterative(input_str_2))
print(str_length_recursive(input_str_2))
