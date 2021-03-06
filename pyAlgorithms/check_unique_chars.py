unique_str = 'AbCDefG'
not_unique_str = 'non Unique STR' 

def normalise(input_str):
	input_str = input_str.replace(' ', '')
	return input_str.lower()

def is_unique_1(input_str):
	d = dict()
	for i in input_str:
		if i in d:
			return False
		else:
			d[i] = 1
	return True


def is_unique_2(input_str):
	return len(set(input_str)) == len(input_str)


def is_unique_3(input_str):
	alpha = 'abcdefghijklmnopqrstuvwxyz'
	for i in input_str:
		if i in alpha:
			alpha = alpha.replace(i, '')
		else:
			return False
	return True
 
unique_str = normalise(unique_str)
not_unique_str = normalise(not_unique_str)

print(is_unique_1(unique_str))
print(is_unique_1(not_unique_str))

print(is_unique_2(unique_str))
print(is_unique_2(not_unique_str))

print(is_unique_3(unique_str))
print(is_unique_3(not_unique_str))