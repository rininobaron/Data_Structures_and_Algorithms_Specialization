def counter():
    n, m = map(int, input().split(" "))
    l_array,r_array=[],[]
    for _ in range(n):
        l, r = map(int, input().split(" "))
        l_array.append(l)
        r_array.append(r)
    points = input().split(" ")
    points_int=[int(i) for i in points]
    if len(points) != m:
        return print(f"ERROR!\nThe number of points are not {m}")
    map_ref=list(zip(l_array*m,r_array*m, points_int*n))
    map_ref=list(map(lambda x: [sorted([x[0]]+[x[1]]+[x[2]]), x[2]], map_ref))
    counter_dict={point:0 for point in points}
    for array in map_ref:
        if array[0][1]==array[1]:
            counter_dict[str(array[1])]+=1
    return print(" ".join([str(i) for i in counter_dict.values()]))

counter()
