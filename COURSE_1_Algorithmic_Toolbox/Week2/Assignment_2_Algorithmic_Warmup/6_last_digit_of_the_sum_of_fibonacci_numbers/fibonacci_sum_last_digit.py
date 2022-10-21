def last_digit_of_the_sum_of_fibos(n):
	if n <= 1:
		return n
	Fn_2 = 0
	Fn_1 = 1
	fibo_sum = 1
	for _ in range(2, n+1):
		Fn = (Fn_2 + Fn_1)%10
		Fn_2, Fn_1 = Fn_1, Fn
		fibo_sum += Fn
	return fibo_sum%10

print(last_digit_of_the_sum_of_fibos(int(input(''))))