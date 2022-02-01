# count the number of constanants in a string

input_str_3 = 'aeioj'
vowels = 'aekbiou'

def count_constanants_iterative(input_str):
	count = 0
	for i in input_str:
		if i not in vowels and i.isalpha():
			count += 1
	return count

def count_constanants_recursive(input_str):
	if input_str == '':
		return 0 
	if input_str[0].lower() not in vowels and input_str[0].isalpha():
		return 1 + count_constanants_recursive(input_str[1:])
	else:
		return count_constanants_recursive(input_str[1:])

print(count_constanants_iterative(input_str_3))
print(count_constanants_recursive(input_str_3))
