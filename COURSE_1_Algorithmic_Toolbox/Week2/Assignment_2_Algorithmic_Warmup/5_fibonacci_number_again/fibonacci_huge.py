def fibo(n):
	if n <= 1:
		return n
	Fn_2 = 0
	Fn_1 = 1
	for _ in range(n-1):
		Fn = Fn_2 + Fn_1
		Fn_2, Fn_1 = Fn_1, Fn
	return Fn

def pisano(m):
	Fn_2 = 0
	Fn_1 = 1
	for i in range(m**2):
		Fn = (Fn_2 + Fn_1)%m
		Fn_2, Fn_1 = Fn_1, Fn
		# A Pisano Period starts with 01
		if Fn_2 == 0 and Fn_1 == 1:
			return i + 1

def huge_fibo(n, m):
	return fibo(n%pisano(m))%m
	
n, m = map(int, input('').split(' '))
#n = int(input(''))
print(huge_fibo(n, m))