A = [1, 2, 3, 4, 5, 4, 3, 2, 1]

def linear_bitonic_peak_search(A): # Time O(n) : Space O(1)

	if len(A) < 3:
		return None

	for i in range(len(A) - 1):
		if i != 0 and (A[i - 1] < A[i] and A[i + 1] < A[i]):
			return A[i]
	return None

def find_highest_num(A):
	low = 0
	high = len(A) - 1

	if len(A) < 3:
		return None

	while low <= high:
		mid = (low + high) // 2

		if mid - 1 > 0:
			mid_left = A[mid - 1]
		else: 
			float('-inf')
		
		if mid + 1 < len(A) - 1:
			mid_right = A[mid + 1]
		else: 
			float('inf')

		if mid_left < A[mid] and mid_right > A[mid]:
			low = mid + 1

		elif mid_left > A[mid] and mid_right < A[mid]:
			high = mid - 1

		elif mid_left < A[mid] and mid_right < A[mid]:
			return A[mid]

	return None

print(linear_bitonic_peak_search(A))
print(find_highest_num(A))
