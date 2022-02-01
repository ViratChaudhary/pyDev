data = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]

def func(data):
	min_price_so_far = float('inf')
	max_profit = 0

	for price in data:
		max_profit_sell_today = price - min_price_so_far
		max_profit = max(max_profit, max_profit_sell_today)
		min_price_so_far = min(min_price_so_far, price)

	return max_profit

	