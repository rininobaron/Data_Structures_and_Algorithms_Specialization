def euclideanGCM(a, b):
	if a == 0 or b == 0:
		return max(a, b)
	a2 = max(a, b)
	b2 = min(a, b)
	c = a2%b2
	return euclideanGCM(b2, c)

a, b = map(int, input().split())
print(a*b//euclideanGCM(a, b))