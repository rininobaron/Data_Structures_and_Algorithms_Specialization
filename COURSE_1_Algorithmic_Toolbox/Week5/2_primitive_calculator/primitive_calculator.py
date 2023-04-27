def calculator(n):
	if n == 1:
		return print("0\n1")
	iter_dict={'0':[n]}
	listIndexes=[[None]]
	i=1
	while 1 not in iter_dict[str(i-1)]:
		iter_dict[str(i)]=[]
		tempIndexes=[]
		for j in range(len(iter_dict[str(i-1)])):
			if iter_dict[str(i-1)][j]>1:
				iter_dict[str(i)].append(iter_dict[str(i-1)][j] - 1)
				tempIndexes.append(j)
			if iter_dict[str(i-1)][j]%2==0:
				iter_dict[str(i)].append(iter_dict[str(i-1)][j]/2)
				tempIndexes.append(j)
			if iter_dict[str(i-1)][j]%3==0:
				iter_dict[str(i)].append(iter_dict[str(i-1)][j]/3)
				tempIndexes.append(j)
		listIndexes.append(tempIndexes)
		i+=1
	i-=1
	intermediateNumbers=[]
	index=iter_dict[str(i)].index(1)
	next_index=listIndexes[i][index]
	intermediateNumbers.append(1)
	i-=1
	while i>0:
		intermediateNumbers.append(int(iter_dict[str(i)][next_index]))
		next_index=listIndexes[i][next_index]
		i-=1
	intermediateNumbers.append(n)
	#print(intermediateNumbers)
	#print(len(intermediateNumbers)-1)
	# print()
	# print("len dict: "+str(len(iter_dict.keys())))
	# print("len indexes: "+str(len(listIndexes)))
	# print(i)
	# for i in range(len(iter_dict.keys())):
	# 	#print("Indexes")
	# 	#print(i, len(listIndexes[i]))
	# 	print(listIndexes[i])
	# 	print("Numbers")
	# 	print(i, len(iter_dict[str(i)]))
	# 	print(iter_dict[str(i)])
	counterNumers=len(intermediateNumbers)-1
	intermediateNumbers=" ".join([str(i) for i in intermediateNumbers])
	return print(str(counterNumers)+"\n"+intermediateNumbers)

n = int(input())
calculator(n)