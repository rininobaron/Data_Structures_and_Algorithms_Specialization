from itertools import combinations

def distance(point1,point2):
	d=((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)**(1/2)
	return d

def min_partial_distance(points):
	min_d = float("inf")
	for point1, point2 in combinations(points, 2):
		min_d = min(min_d, distance(point1, point2))
	return min_d

def strip_points(half_x,d):
	def calculate_distance(point):
		return abs(point[0]-half_x)<=d
	return calculate_distance

def min_final_distance(points,d):
	min_d=float("inf")
	for i in range(len(points)):
		j=i+1
		while j<=7:
			if j==len(points):
				break
			d_prime=distance(points[i],points[j])
			if d_prime<min_d:
				min_d=d_prime
			if min_d>=d:
				break
			j+=1
	return min_d

def min_global_distance(points):
	if len(points)<=3:
		return min_partial_distance(points)
	n=len(points)
	points1=points[:n//2]
	points2=points[n//2:]
	half_x=points[n//2][0]
	#min_d1=min_partial_distance(points1)
	#min_d2=min_partial_distance(points2)
	min_d1=min_global_distance(points1)
	min_d2=min_global_distance(points2)
	d=min(min_d1,min_d2)
	points1=list(filter(strip_points(half_x,d),points1))
	points2=list(filter(strip_points(half_x,d),points2))
	points=points1+points2
	points = sorted(points, key=lambda point: point[1])
	d_prime=min_final_distance(points,d)
	min_final_d=min(d,d_prime)
	return min_final_d

n=int(input(""))
points=[]
for _ in range(n):
	x,y=map(int,input("").split(" "))
	points.append((x,y))
points.sort()
print(min_global_distance(points))