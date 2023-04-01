import time

def merge(array1, array2):
	counter=0
	array=[]
	while len(array1)>0 and len(array2)>0:
		if array1[0]<=array2[0]:
			array.append(array1[0])
			array1.remove(array1[0])
		else:
			counter+=len(array1)
			array.append(array2[0])
			array2.remove(array2[0])
	return counter

def sort_count_swaps(array):
	array2=[]
	counter=0
	while len(array)>0:
		minIndex=0
		value=min(array)
		minIndex=array.index(value)
		# for j in range(1,len(array)):
		# 	if array[j] < array[minIndex]:
		# 		minIndex=j
		array2.append(array[minIndex])
		array.remove(array[minIndex])
		if minIndex!=0:
			counter+=minIndex
	return array2,counter

def counter():
	n=int(input(""))
	array=input("")
	array=array.split(" ")
	array=[int(i) for i in array]
	if len(array)!=n:
		return print("ERROR!\nThe length of array is not "+str(n))
	m=len(array)//2
	array1=array[:m].copy()
	array2=array[m:].copy()
	array1,counter1=sort_count_swaps(array1)
	array2,counter2=sort_count_swaps(array2)
	counter=merge(array1,array2)
	return print(counter+counter1+counter2)

counter()