A = [-10, -5, 0, 3, 7]

def find_fixedpoint_linear(A): # Time O(n) Space O(1)
	for i in range(len(A)):
		if A[i] == i:
			return A[i]
	return None 

def find_fixedpoint(A): # Time O(log n) Space O(1)
	low = 0
	high = len(A) - 1

	while low <= high:
		mid = (low + high) // 2
		if A[mid] < mid:
			low = mid + 1
		elif A[mid] > mid:
			high = mid - 1
		else:
			return A[mid]

	return None

print(find_fixedpoint_linear(A))
print(find_fixedpoint(A))