def dp_change(money, coins):
	minNumCoins = {'0':0}
	for m in range(1, money+1):
		minNumCoins[str(m)] = float("inf")
		for coin in coins:
			if m >= coin:
				numCoins = minNumCoins[str(m-coin)] + 1
				if numCoins < minNumCoins[str(m)]:
					minNumCoins[str(m)] = numCoins
	return print(minNumCoins[str(money)])

money = int(input())
coins = [1, 3, 4]
dp_change(money, coins)