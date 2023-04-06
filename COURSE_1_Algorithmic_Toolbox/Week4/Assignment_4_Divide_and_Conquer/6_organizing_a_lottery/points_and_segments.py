def counter():
	n,m=input("").split(" ")
	n,m=int(n),int(m)
	segments=[]
	for _ in range(n):
		l,r=input("").split(" ")
		segments.append([int(l),int(r)])
	points=input("").split(" ")
	if len(points)!=m:
		return print("ERROR!\nThe number of pints are not "+str(m))
	counter_list=[]
	for point in points:
		counter=0
		for seg in segments:
			if int(point) in range(seg[0],seg[1]+1):
				counter+=1
		counter_list.append(counter)
	return print(" ".join([str(i) for i in counter_list]))

counter()