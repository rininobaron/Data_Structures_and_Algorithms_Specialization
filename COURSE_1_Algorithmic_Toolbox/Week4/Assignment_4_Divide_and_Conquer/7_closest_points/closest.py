def min_partial_distance(points,half_x):
	min_d=float("inf")
	distances=[]
	counter=0
	for point in points:
		for index,point2 in enumerate(points):
			if counter==index:
				continue
			d=((point[0]-point2[0])**2+(point[1]-point2[1])**2)**(1/2)
			if d<min_d:
				min_d=d
		counter+=1
		distances.append(abs(point[0]-half_x))
	return min_d, distances

def strip_points(points,distances,d):
	points_final=[]
	for index,distance in enumerate(distances):
		if distance<=d:
			points_final.append(points[index])
	return points_final

def min_final_distance(points):
	min_d=float("inf")
	counter=0
	for point in points:
		for index,point2 in enumerate(points):
			if counter==index:
				continue
			d=((point[0]-point2[0])**2+(point[1]-point2[1])**2)**(1/2)
			if d<min_d:
				min_d=d
		counter+=1
	return min_d

def min_global_distance():
	n=int(input(""))
	X,Y=[],[]
	for _ in range(n):
		x,y=map(int,input("").split(" "))
		X.append(x)
		Y.append(y)
	points=list(zip(X,Y))
	points.sort()
	points1=points[:len(X)//2]
	points2=points[len(X)//2:]
	#half_x=(points1[-1][0]+points2[0][0])/2
	#half_x=(max(X)+min(X))/2
	half_x=points[len(X)//2][0]
	min_d1,distances1=min_partial_distance(points1,half_x)
	min_d2,distances2=min_partial_distance(points2,half_x)
	d=min(min_d1,min_d2)
	points1=strip_points(points1,distances1,d)
	points2=strip_points(points2,distances2,d)
	points=points1+points2
	points = sorted(points, key=lambda point: point[1])
	min_final_d=min_final_distance(points)
	return print(min_final_d)

min_global_distance()