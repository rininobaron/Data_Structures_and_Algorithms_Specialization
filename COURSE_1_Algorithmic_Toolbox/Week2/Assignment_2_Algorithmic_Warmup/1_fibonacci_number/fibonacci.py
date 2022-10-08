def fibonacci(n):
	if n <= 1:
		return n
	Fn_2 = 0
	Fn_1 = 1
	for _ in range(n-1):
		Fn = Fn_2 + Fn_1
		Fn_2, Fn_1 = Fn_1, Fn
	return Fn
print(fibonacci(int(input(''))))