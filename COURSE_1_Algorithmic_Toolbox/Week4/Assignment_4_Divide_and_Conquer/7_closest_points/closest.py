def min_partial_distance(points,half_x):
	min_d=10**9
	distances=[]
	for point in points:
		for point2 in points:
			if point==point2:
				continue
			d=((point[0]-point2[0])**2+(point[1]-point2[1])**2)**(1/2)
			if d<min_d:
				min_d=d
		distances.append(abs(point[0]-half_x))
	return min_d, distances

def strip_points(points,distances,d):
	points_final=[]
	for index,distance in enumerate(distances):
		if distance<=d:
			points_final.append(points[index])
	return points_final

def min_final_distance(points):
	min_d=10**9
	for point in points:
		for point2 in points:
			if point==point2:
				continue
			d=((point[0]-point2[0])**2+(point[1]-point2[1])**2)**(1/2)
			if d<min_d:
				min_d=d
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
	if len(X)%2==0:
		half_x=(points[int(len(X)/2)][0]+points[int(len(X)/2-1)][0])/2
	else:
		half_x=points[len(X)//2][0]
	points1,points2=[],[]
	for point in points:
		if point[0]<half_x:
			points1.append(point)
		else:
			points2.append(point)
	min_d1,distances1=min_partial_distance(points1,half_x)
	min_d2,distances2=min_partial_distance(points2,half_x)
	d=min(min_d1,min_d2)
	points1=strip_points(points1,distances1,d)
	points2=strip_points(points2,distances2,d)
	points=points1+points2
	min_final_d=min_final_distance(points)
	return print(min_final_d)

min_global_distance()