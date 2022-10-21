def fibo(n):
	if n <= 1:
		return n
	Fn_2 = 0
	Fn_1 = 1
	for _ in range(n-1):
		Fn = Fn_2 + Fn_1
		Fn_2, Fn_1 = Fn_1, Fn
	return Fn

def sum_fibo_squares(n):
	fibo_n = fibo(n)
	fibo_sum = fibo_n*(fibo_n + fibo(n-1))
	return fibo_sum%10

print(sum_fibo_squares(int(input(''))))