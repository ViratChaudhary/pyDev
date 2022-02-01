# Palindrome Standard Reverse Problem

input_str = 'Was it a cat I saw?'

# the below solution works but requires more space

#s = ''.join([i for i in input_str if i.isalpha()]).lower()
#print(s == s[::-1]) 



def is_palindrome(input_str):
	i = 0
	j = len(input_str) - 1

	while i < j:
		while not input_str[i].isalnum() and i < j:
			i += 1
		while not input_str[j].isalnum() and i < j:
			j -= 1
		if input_str[i].lower() != input_str[j].lower():
			return False
		i += 1
		j -= 1

	return True 

print(is_palindrome(input_str))




# Palindrome Permutation Problem

input_str_2 = 'Tact Coa'

def is_palin_perm(input_str):
	input_str = input_str.replace(' ', '').lower()

	d = dict()

	for i in input_str:
		if i in d:
			d[i] += 1
		else:
			d[i] = 1

	print(d)

	odd_count = 0
	for k, v in d.items():
		if v % 2 != 0 and odd_count == 0:
			odd_count += 1
		else: # finding another odd number and odd_count != 0
			return False 

	return True

is_palin_perm(input_str_2)

