l1 = [1, 3, 4, 5, 9, 10, 15, 19, 21, 24, 25, 29, 100]
target = 30

def closest_num_solution(l1, target):
	min_diff = float('inf')
	low = 0
	high = len(l1) - 1
	closest_number = None

	if len(l1) == 0:
		return None
	if len(l1) == 1:
		return l1[0] 	

# iteration of the main loop
	while low <= high:
		mid = (low + high) // 2

		if mid + 1 < len(l1):
			min_diff_right = abs(l1[mid + 1] - target)
		if mid > 0:
			min_diff_left = abs(l1[mid - 1] - target)

		if min_diff_left < min_diff:
			min_diff = min_diff_left
			closest_number = l1[mid - 1]

		if min_diff_right < min_diff:
			min_diff = min_diff_right
			closest_number = l1[mid + 1]

		if l1[mid] < target:
			low = mid + 1
		elif l1[mid] > target:
			high = mid - 1
		else:
			return l1[mid]

	return closest_number

print(closest_num_solution(l1, target))


