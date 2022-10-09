def gcd(n, m):
	if m == 0:
		return n
	while m != 0:
		n, m = m, n%m
	return n

n, m = map(int, input('').split(' '))
print(gcd(n, m))