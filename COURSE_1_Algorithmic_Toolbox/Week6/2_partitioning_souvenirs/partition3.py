def max_amount2(W,n,weights):
	value=[[0]*(n+1) for _ in range(W+1)]
	v=weights.copy()
	for i in range(1,n+1):
		for w in range(1,W+1):
			value[w][i]=value[w][i-1]
			if weights[i-1]<=w:
				val=value[w-weights[i-1]][i-1] + v[i-1]
				if value[w][i] < val:
					value[w][i]=val
	final_list=[]
	while i>=1 and w>=1:
		val=value[w-weights[i-1]][i-1] + v[i-1]
		val2=value[w][i-1]
		if w-weights[i-1]<0:
			i-=1
			continue
		if val > val2:
			final_list.append(v[i-1])
			w=w-weights[i-1]
			i-=1
		else:
			i-=1
	return value[-1][-1], list(reversed(final_list))


def split_loot(n, numbers):
	if len(numbers)<3:
		return 0
	if sum(numbers)%3!=0:
		return 0
	target=int(sum(numbers)/3)
	for i in range(3):
		result, temp_list=max_amount2(target,len(numbers),numbers)
		if result!=target:
			return 0
		for number in temp_list:
			numbers.remove(number)
	return 1

n=int(input())
numbers=input().split()
numbers=[int(i) for i in numbers]
if n!=len(numbers):
	print("ERROR!\nThe total numbers are not "+str(n))
	exit()
print(split_loot(n, numbers))