def can_split_into_three_sets(numbers):
    if len(numbers)<3:
        return 0
    total_sum = sum(numbers)
    if total_sum % 3 != 0:
        return 0
    target_sum = total_sum // 3
    set_sums = [0, 0, 0]
    return backtrack(numbers, 0, set_sums, target_sum)

def backtrack(numbers, index, set_sums, target_sum):
    if index == len(numbers):
        return set_sums[0] == set_sums[1] == set_sums[2] == target_sum
    for i in range(3):
        if set_sums[i] + numbers[index] <= target_sum:
            set_sums[i] += numbers[index]
            if backtrack(numbers, index + 1, set_sums, target_sum):
                return 1
            set_sums[i] -= numbers[index]
    return 0

n=int(input())
numbers=input().split()
numbers=[int(i) for i in numbers]
if n!=len(numbers):
    print("ERROR!\nThe total numbers are not "+str(n))
    exit()
print(can_split_into_three_sets(numbers))