'''
This function calculate the minimum number of coins with values 1,2,5
needed to change a given auanity of money
'''
def change(money):
	if money == 0:
		return 0
	denom = [1,2,5]
	maxCoin = max(denom)
	while maxCoin > money:
		denom.remove(maxCoin)
		maxCoin = max(denom)
	money -= maxCoin
	return 1 + change(money)

print(change(int(input(''))))