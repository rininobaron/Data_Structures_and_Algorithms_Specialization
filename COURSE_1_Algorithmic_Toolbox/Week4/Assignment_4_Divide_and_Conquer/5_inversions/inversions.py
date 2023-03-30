import random

def swap(array, i, minIndex):
	temp=array[i]
	array[i]=array[minIndex]
	array[minIndex]=temp
	return array

def selection_sort(array):
	counter=0
	for i in range(len(array)):
		minIndex=i
		for j in range(i+1,len(array)):
			if array[j] < array[minIndex]:
				minIndex=j
		if i != minIndex:
			array = swap(array, i, minIndex)
			counter+=1
	return array, counter

def radomized_quick_sort():
	n=int(input(""))
	array=input("")
	array=array.split(" ")
	array=[int(i) for i in array]
	if len(array)!=n:
		return print("ERROR!\nThe length of array is not "+str(n))
	array,counter=selection_sort(array)
	return print(counter)

radomized_quick_sort()