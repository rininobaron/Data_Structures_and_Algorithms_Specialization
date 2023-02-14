def min_refills(d,m,n_stops,stops):
	'''
	INPUT:
		d: final distance (integer)
		m: miles on a full tank (integer)
		n_stops: number of stops (integer)
		stops: list of stops
	OUTPUT:
		refills: minimum number of refills (integer)
	'''
	if m < stops[0]:
		return -1
	original_m = m
	refills = 0
	for i in range(n_stops):
		if i == 0:
			prev_stop = 0
			current_stop = stops[i]
			next_stop = stops[i+1]
		elif i == n_stops-1:
			prev_stop = stops[i-1]
			current_stop = stops[i]
			next_stop = d
		else:
			prev_stop = stops[i-1]
			current_stop = stops[i]
			next_stop = stops[i+1]
		diff = next_stop - current_stop
		diff2 = current_stop - prev_stop
		m -= diff2
		if m < diff:
			refills+=1
			m = original_m
			if m < diff:
				# The next stop is too far!
				return -1
	return refills

# Get data from user
d = int(input(""))
m = int(input(""))
n_stops = int(input(""))
stops = input("")
stops = stops.split(" ")
stops = [int(i) for i in stops]
if len(stops) != n_stops:
	print("ERROR!\nNumber of stops are not correct!")
	exit()
if stops[-1] >= d:
	print("ERROR!\nThe last stop is not before the destine!")
	exit()
for i in range(len(stops)):
	if i == 0:
		continue
	if stops[i-1] >= stops[i]:
		print("ERROR!\nThe stops must be in incremental order!")
		exit()
print(min_refills(d,m,n_stops,stops))