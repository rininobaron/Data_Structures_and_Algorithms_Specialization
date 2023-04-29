def lcsv2(a, b):
	T=[[0]*(len(b)+1) for _ in range(len(a)+1)]
	for i in range(1, len(a)+1):
		for j in range(1, len(b)+1):
			if a[i-1]==b[j-1]:
				T[i][j]=T[i-1][j-1]+1
			else:
				T[i][j]=max(T[i][j-1], T[i-1][j], T[i-1][j-1])
	return T[len(a)][len(b)]

n = int(input())
a = input().split()
a = [int(i) for i in a]
if n != len(a):
	print("Error!\nThe sequence doesn't have {} numbers".format(n))
	exit()
m = int(input())
b = input().split()
b = [int(i) for i in b]
if m != len(b):
	print("Error!\nThe sequence doesn't have {} numbers".format(m))
	exit()
print(lcsv2(a, b))