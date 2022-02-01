# product using recursion

x = 5
y = 3

def product_iterate(x, y):
	answ = 0
	for i in range(y):
		answ += x
	return answ

def product_recursion(x, y): 

	if x < y: # cant take away the load by doing two seperate recursive calls alternatively
		product_recursion(y, x)

	if y == 0: # cant handle high values --> to many recursive calls (see above code to fix)
		return 0
	return x + product_recursion(x, y - 1)

print(product_recursion(x, y))
print(product_iterate(x, y))