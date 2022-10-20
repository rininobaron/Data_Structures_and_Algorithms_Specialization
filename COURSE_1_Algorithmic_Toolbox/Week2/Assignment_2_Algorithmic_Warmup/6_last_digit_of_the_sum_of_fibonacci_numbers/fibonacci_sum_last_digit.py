def fibo(n):
	if n <= 1:
		return n
	Fn_2 = 0
	Fn_1 = 1
	for _ in range(n-1):
		Fn = Fn_2 + Fn_1
		Fn_2, Fn_1 = Fn_1, Fn
	return Fn

def last_digit_of_the_sum_of_fibos(n):
	fibo_sum = 0
	for i in range(n+1):
		fibo_sum += fibo(i)
	return fibo_sum%10

print(last_digit_of_the_sum_of_fibos(int(input(''))))