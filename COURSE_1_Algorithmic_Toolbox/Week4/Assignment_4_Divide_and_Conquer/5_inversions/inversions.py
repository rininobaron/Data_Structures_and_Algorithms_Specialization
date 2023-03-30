def swap(array, i, minIndex):
	temp=array[i]
	array[i]=array[minIndex]
	array[minIndex]=temp
	return array

def count_swaps(array):
	counter=0
	counterFlag=0
	while counterFlag!=len(array):
		counterFlag=0
		for i in range(len(array)):
			if i==len(array)-1:
				counterFlag+=1
				continue
			if array[i] > array[i+1]:
				array = swap(array, i, i+1)
				counter+=1
			else:
				counterFlag+=1
	return counter

def counter():
	n=int(input(""))
	array=input("")
	array=array.split(" ")
	array=[int(i) for i in array]
	if len(array)!=n:
		return print("ERROR!\nThe length of array is not "+str(n))
	counter=count_swaps(array)
	return print(counter)

counter()