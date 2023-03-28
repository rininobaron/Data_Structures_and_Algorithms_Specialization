import random

def swap(array, i, minIndex):
	temp=array[i]
	array[i]=array[minIndex]
	array[minIndex]=temp
	return array

def selection_sort(array):
	for i in range(len(array)):
		minIndex=i
		for j in range(i+1,len(array)):
			if array[j] < array[minIndex]:
				minIndex=j
		array = swap(array, i, minIndex)
	return array

def radomized_quick_sort():
	n=int(input(""))
	array=input("")
	array=array.split(" ")
	array=[int(i) for i in array]
	if len(array)!=n:
		return print("ERROR!\nThe length of array is not "+str(n))
	m=random.choice(array)
	array1=[]
	array2=[]
	for i in range(len(array)):
		if array[i] <=m:
			array1.append(array[i])
		else:
			array2.append(array[i])
	array1=selection_sort(array1)
	array2=selection_sort(array2)
	array=array1+array2
	array=[str(i) for i in array]
	return print(" ".join(array))

radomized_quick_sort()