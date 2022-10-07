def gcd(a, b):
	if b == 0:
		return a, 0
	return b, a%b

a=357
b=234
while b != 0:
	a,b = gcd(a,b)

print(a,b)