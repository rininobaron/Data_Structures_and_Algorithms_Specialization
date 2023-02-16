def max_dot_product(n, prices, clicks):
	dot_product = 0
	while n > 0:
		max_p = max(prices)
		max_c = max(clicks)
		dot_product += max_p*max_c
		prices.pop(prices.index(max_p))
		clicks.pop(clicks.index(max_c)) 
		n-=1
	return dot_product

# Get data from user
n = int(input(""))
prices = input("")
clicks = input("")
prices = prices.split(" ")
prices = [int(i) for i in prices]
clicks = clicks.split(" ")
clicks = [int(i) for i in clicks]
if len(prices) != n:
	print("ERROR\nThe prices are not "+str(n))
	exit()
elif len(clicks) != n:
	print("ERROR\nThe clicks are not "+str(n))
	exit()
print(max_dot_product(n, prices, clicks))


