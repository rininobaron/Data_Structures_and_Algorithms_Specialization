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
	return value

def split_loot(n, numbers):
	if len(numbers)<3:
		return 0
	if sum(numbers)%3!=0:
		return 0
	third_W=int(sum(numbers)/3)
	value=max_amount(sum(numbers),len(numbers),numbers)
	if value[third_W][-1]==third_W and value[2*third_W][-1]==2*third_W and value[3*third_W][-1]==3*third_W:
		return 1
	else:
		return 0

n=int(input())
numbers=input().split()
numbers=[int(i) for i in numbers]
if n!=len(numbers):
	print("ERROR!\nThe total numbers are not "+str(n))
	exit()
print(split_loot(n, numbers))