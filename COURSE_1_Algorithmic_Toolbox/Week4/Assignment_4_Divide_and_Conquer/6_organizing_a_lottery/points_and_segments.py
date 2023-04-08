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
	counter_diff=set(points).difference(set(counter_dict.keys()))
	for point in points:
		if point in counter_diff:
			counter_list.append(str(0))
			continue
		counter_list.append(str(counter_dict[point]))
	return print(" ".join(counter_list))

counter()