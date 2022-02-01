# find the uppercase letter

input_str_1 = 'viratChaudhary'

def find_uppercase_iterative(input_str):
	for i in input_str:
		if i.isupper():
			return i 
	return 'No uppercase character found'

def find_uppercase_recursive(input_str, index=0):
	if input_str[index].isupper():
		return input_str[index]
	if index == len(input_str) - 1:
		return 'no uppercases found'
	return find_uppercase_recursive(input_str, index + 1)

print(find_uppercase_iterative(input_str_1))
print(find_uppercase_recursive(input_str_1))




