def huge_fibo(n, m):
	if n <= 1:
		return n%m
	Fn_2 = 0
	Fn_1 = 1
	for _ in range(n-1):
		Fn = (Fn_2 + Fn_1)%m
		Fn_2, Fn_1 = Fn_1, Fn
	return Fn
	
n, m = map(int, input('').split(' '))
print(huge_fibo(n, m))