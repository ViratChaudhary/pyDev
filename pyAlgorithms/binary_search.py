data = [3, 4, 6, 10, 21, 25, 29, 30, 32, 33, 38, 41]
target = 33

# Linear Search

def linear_search(data, target):
	for i in range(len(data)):
		 if data[i] == target:
		 	return True
	return False
	
	# O(n) time 

# Iterative Binary Search

def binary_search_iterative(data, target):
	low = 0
	high = len(data) - 1

	while low <= high:
		mid = (low + high) // 2
		if target == data[mid]:
			return True
		elif target < data[mid]:
			high = mid - 1
		else:
			low = mid + 1
	return False 

# Recursive Binary Search

def binary_search_recursive(data, target, low, high):
	
	if low > high:
		return False
	else:
		mid = (low + high) // 2
		if target == data[mid]:
			return True
		elif target < data[mid]:
			return binary_search_recursive(data, target, low, mid - 1)
		else:
			return binary_search_recursive(data, target, mid + 1, high)

print(linear_search(data, target))
print(binary_search_iterative(data, target))
print(binary_search_recursive(data, target, 0, len(data) - 1))

























