def counter():
	n,m=input("").split(" ")
	n,m=int(n),int(m)
	counter_dict={}
	for _ in range(n):
		l,r=input("").split(" ")
		for i in range(int(l),int(r)+1):
			if str(i) not in counter_dict.keys():
				counter_dict[str(i)]=0
			counter_dict[str(i)]+=1
	points=input("").split(" ")
	if len(points)!=m:
		return print("ERROR!\nThe number of points are not "+str(m))
	counter_list=[]
	for point in points:
		try:
			counter_list.append(counter_dict[point])
		except:
			counter_list.append(0)
	return print(" ".join([str(i) for i in counter_list]))

counter()