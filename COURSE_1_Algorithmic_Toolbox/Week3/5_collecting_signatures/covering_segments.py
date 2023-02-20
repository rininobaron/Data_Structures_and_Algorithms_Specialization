def get_points():
	# Get data from user
	n = int(input(""))
	counter = 0
	pairs = []
	while n != counter:
		pair = input("")
		pair = pair.split(" ")
		pair = [int(i) for i in pair]
		if len(pair) != 2:
			return "ERROR!\nThe input is not an integer pair"
		if pair[0] > pair[1]:
			return "ERROR!\nFirst number must be less or equal than second"
		pairs.append(pair)
		counter+=1
	# Sort pairs by r (pair[1]) in ascending order
	pairs_copy = pairs.copy()
	pairs_sort = []
	while len(pairs) > 0:
		pair_min_r = pairs[0]
		target_index = 0
		counter = 0
		for pair in pairs:
			if counter == 0:
				counter+=1
				continue
			if pair[1] < pair_min_r[1]:
				pair_min_r = pair
				target_index = counter
			if pair[1] == pair_min_r[1]:
				if pair[0] < pair_min_r[0]:
					pair_min_r = pair
					target_index = counter
			counter+=1
		pairs_sort.append(pair_min_r)
		pairs.pop(target_index)
	# Appen index to each pair in pairs_sort
	indexes = list(range(len(pairs_sort)))
	for index,_ in enumerate(pairs_sort):
		pairs_sort[index].append(index)
	# Look for minimum points
	start = pairs_sort[0][0]
	final_points = []
	#print(pairs_sort)
	while len(pairs_sort) > 0:
		temp_dict = {}
		for pair in pairs_sort:
			if start > pair[1]:
				start = pair[0]
			#print("start: "+str(start))
			for point in range(start,pair[1]+1):
				for pair_j in pairs_sort:
					if pair_j[0] <= point and pair_j[1] >= point:
						if point not in temp_dict.keys():
							temp_dict[point] = []
						temp_dict[point].append(pair_j[2])
		# Look for the point with more segments "touched"
		# If there are many points, the maximum is choice
		target_len = 0
		final_point = 0
		for point in temp_dict.keys():
			if target_len < len(temp_dict[point]):
				final_point = point
				target_len = len(temp_dict[point])
			elif target_len == len(temp_dict[point]):
				if final_point < point:
					final_point=point
					target_len = len(temp_dict[point])
		# Remove the pairs (segments) "touched" by the point
		for index in temp_dict[final_point]:
			for pair in pairs_sort:
				if pair[2] == index:
					pairs_sort.remove(pair)
		start = max(temp_dict.keys())+1
		final_points.append(final_point)
		#print(temp_dict)
	final_points.sort()
	final_points = list(set(final_points))
	#print()
	#print(final_points)
	return final_points 


final_points = get_points()
len_ = len(final_points)
final_points = " ".join([str(i) for i in final_points])
print(len_)
print(final_points)