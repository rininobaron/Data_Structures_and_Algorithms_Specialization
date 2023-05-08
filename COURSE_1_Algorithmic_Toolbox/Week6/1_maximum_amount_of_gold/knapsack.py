def max_amount(W,n,weights):
	weights=sorted(weights)
	weights.reverse()
	remainW=W
	for w in weights:
		if w <= remainW:
			remainW-=w
	return W-remainW

W, n = input().split()
W, n = int(W), int(n)
weights = input().split()
weights = [int(i) for i in weights]
if len(weights)!=n:
	print("ERROR!\nThe total weights are not "+str(n))
	exit()
print(max_amount(W,n,weights))