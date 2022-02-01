from stack import Stack

# example = 242 # evaluting the remainders by dividing by 2

# 242 / 2 = 121  --> 0
# 121 / 2 = 60   --> 1
# 60 / 2 = 30    --> 0
# 30 / 2 = 15    --> 0
# 15 / 2 = 7     --> 1
# 7 / 2 = 3      --> 1
# 3 / 2 = 1      --> 1
# 1 / 2 = 0      --> 1

def div_by_2(dec_num):
	s = Stack()

	while dec_num > 0:
		remainder  = dec_num % 2
		s.push(remainder)
		dec_num = dec_num / 2

	bin_num = ''
	while not s.is_empty():
		bin_num += str(s.pop())

	return bin_num

print(div_by_2(241))