def gcd(n, m):
	if m == 0:
		return n, 0
	while m != 0:
		n, m = m, n%m
	return n

n, m = map(int, input('').split(' '))
print(huge_fibo_number(n, m))