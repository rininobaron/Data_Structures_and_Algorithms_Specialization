
def maximum_loot(W, costs_weigths2):
	'''
	Input format. The first line of the input contains 
	the number n of compounds and the capacity W of a backpack. 
	The next n lines define the costs and weights of the compounds. 
	The i-th line contains the cost c i and the weight w_i of 
	the i-th compound.

	Output format. Output the maximum value of compounds that fit 
	into the backpack.
	'''
	if W == 0:
		return 0
	if len(costs_weigths2) == 0:
		return 0
	# Compare current weight with W
	# Remember costs_weigths2 is [[c_1,w_1,coeff_1], ... ,[c_n,w_n,coeff_n]]
	subtotal = 0
	if costs_weigths2[0][1] >= W:
		return W*costs_weigths2[0][2]
	else:
		subtotal = costs_weigths2[0][1]*costs_weigths2[0][2]
		W -= costs_weigths2[0][1]
		costs_weigths2.pop(0)
	return subtotal + maximum_loot(W, costs_weigths2)

# Get data from user
n_W = input('')
temp = n_W.split(" ")
if len(temp) != 2:
	print("Error!\nYou must write only two integers parameters")
	exit()
temp = [int(i) for i in temp]
[n, W] = temp
costs_weigths = []
coeff = []
for _ in range(n):
	temp = input('')
	temp = temp.split(" ")
	if len(temp) != 2:
		print("Error!\nYou must write only two integers parameters")
		exit()
	else:
		temp = [int(i) for i in temp]
		# Calculate cost_weigth coefficient
		coeff.append(temp[0]/temp[1])
		costs_weigths.append(temp)
#print(costs_weigths)

# Sort by better cost_weigth coefficient
costs_weigths2 = [] # Also include sort coefficients
#print(costs_weigths)
#print(coeff)
while len(costs_weigths) > 0:
	a = max(coeff)
	index = coeff.index(a)
	costs_weigths2.append([costs_weigths[index][0], costs_weigths[index][1], a])
	coeff.pop(index)
	costs_weigths.pop(index)
#print(costs_weigths2)

print(maximum_loot(W, costs_weigths2))
