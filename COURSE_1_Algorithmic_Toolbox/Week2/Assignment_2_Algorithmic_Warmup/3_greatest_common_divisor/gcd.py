def huge_fibo_number(n, m):
	final_gcd = 1
	for d in range(2, min(n, m) + 1):
		if n%d == 0 and m%d == 0:
			if final_gcd < d:
				final_gcd = d
	return final_gcd
n, m - map(int(), input('').split(' '))
print(huge_fibo_number(n, m))