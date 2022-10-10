def lcm(a, b):
	lcm = 0
	for i in range(2, a*b + 1):
		if i%a == 0 and i%b == 0:
			lcm = i
			break
	return lcm
a, b = map(int, input().split())
print(lcm(a, b))