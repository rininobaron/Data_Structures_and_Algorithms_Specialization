def lcsv3(a, b, c):
	T=[[[0]*(len(c)+1) for _ in range(len(b)+1)] for _ in range(len(a)+1)]
	for i in range(1, len(a)+1):
		for j in range(1, len(b)+1):
			for k in range(1, len(c)+1):
				if a[i-1]==b[j-1] and a[i-1]==c[k-1]:
					T[i][j][k]=T[i-1][j-1][k-1]+1
				else:
					T[i][j][k]=max(T[i][j-1][k-1], T[i][j-1][k], T[i][j][k-1], T[i-1][j][k-1], T[i-1][j][k], T[i-1][j-1][k], T[i-1][j-1][k-1])
	return T[len(a)][len(b)][len(c)]

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
l = int(input())
c = input().split()
c = [int(i) for i in c]
if l != len(c):
	print("Error!\nThe sequence doesn't have {} numbers".format(l))
	exit()
print(lcsv3(a, b, c))