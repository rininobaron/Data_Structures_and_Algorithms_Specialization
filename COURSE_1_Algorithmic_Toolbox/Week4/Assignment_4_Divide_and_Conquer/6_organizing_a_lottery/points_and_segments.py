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
    counter_dict={point:0 for point in points}
    for point in points_int:
        for l,r in zip(l_array,r_array):
            temp=sorted([l,r,point])
            if point==temp[1]:
                counter_dict[str(point)]+=1
    return print(" ".join([str(i) for i in counter_dict.values()]))

counter()
