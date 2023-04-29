def builder_matrix_t(a, b):
	T=[[float("inf")]*(len(b)+1) for _ in range(len(a)+1)]
	for i in range(len(a)+1):
		T[i][0]=i
	for j in range(len(b)+1):
		T[0][j]=j
	for i in range(1, len(a)+1):
		for j in range(1, len(b)+1):
			if a[i-1]==b[j-1]:
				diff=0
			else:
				diff=1
			T[i][j]=min(T[i][j-1]+1, T[i-1][j]+1, T[i-1][j-1]+diff)
	return T

def counter(T,a,b):
	i=len(a)
	j=len(b)
	counter=0
	while i > 0 or j > 0:
		if T[i][j]==T[i-1][j]+1:
			# Deletion
			i-=1
		elif T[i][j]==T[i][j-1]+1:
			# Insertion
			j-=1
		else:
			if a[i-1]==b[j-1]:
				# Match
				counter+=1
			i-=1
			j-=1
	return counter

def lcsv2(a,b):
	T=builder_matrix_t(a, b)
	counter=counter(T,a,b)
	return print(counter)

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
lcsv2(a, b)