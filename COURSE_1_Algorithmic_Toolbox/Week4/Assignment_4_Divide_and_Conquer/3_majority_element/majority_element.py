def majority_element():
	n = int(input(""))
	array = input("")
	array = array.split(" ")
	array = [int(i) for i in array]
	if n != len(array):
		return print("ERROR!\nThe length of array is not "+str(n))
	n_2 = n/2
	counter_dict={}
	for number in array:
		if number not in counter_dict.keys():
			counter_dict[number]=0
		counter_dict[number]+=1
		if counter_dict[number] > n_2:
			return print(1)
	return print(0)

majority_element()