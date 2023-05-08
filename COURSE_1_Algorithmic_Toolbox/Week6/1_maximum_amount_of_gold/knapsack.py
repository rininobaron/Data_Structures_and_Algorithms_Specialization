def max_amount(W,n,weights):
	value=[[0]*(n+1) for _ in range(W+1)]
	v=weights.copy()
	for i in range(1,n+1):
		for w in range(1,W+1):
			value[w][i]=value[w][i-1]
			if weights[i-1]<=w:
				val=value[w-weights[i-1]][i-1] + v[i-1]
				if value[w][i] < val:
					value[w][i]=val
	return value[-1][-1]

W, n = input().split()
W, n = int(W), int(n)
weights = input().split()
weights = [int(i) for i in weights]
if len(weights)!=n:
	print("ERROR!\nThe total weights are not "+str(n))
	exit()
print(max_amount(W,n,weights))