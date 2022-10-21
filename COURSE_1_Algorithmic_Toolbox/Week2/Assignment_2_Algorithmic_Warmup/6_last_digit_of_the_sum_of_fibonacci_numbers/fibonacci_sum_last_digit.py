def last_digit_of_the_sum_of_fibos(n):
	if n <= 1:
		return n
	Fn_2 = 0
	Fn_1 = 1
	fibo_sum = 0
	for i in range(n+1):
		if i == 0 or i == 1:
			fibo_sum += i
			continue
		Fn = Fn_2 + Fn_1
		Fn_2, Fn_1 = Fn_1, Fn
		fibo_sum += Fn
	return fibo_sum%10

print(last_digit_of_the_sum_of_fibos(int(input(''))))