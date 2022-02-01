k = 

def integer_square_root(k):

	low = 0 
	high = k 

	while low <= high:
		mid = (low + high) // 2
		mid_sqr = mid * mid
		
		if mid_sqr <= k:
			low = mid + 1
		else: # mid_sqr >= k
			high = mid - 1

	#print(low)
	#print(high)

	return high

print(integer_square_root(k))