def euclideanGCM(a, b):
	if a == 0 or b == 0:
		return max(a, b)
	a = max(a, b)
	b = min(a, b)
	c = a%b
	return euclideanGCM(b, c)

a, b = map(int, input().split())
print(a*b//euclideanGCM(a, b))