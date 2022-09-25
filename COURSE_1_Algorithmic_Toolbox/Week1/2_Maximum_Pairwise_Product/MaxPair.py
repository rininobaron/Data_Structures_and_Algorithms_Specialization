def maxPairProduct(user_input):
    
    if len(user_input) < 0:
        return print(0)
    if len(user_input) == 1:
        return print(user_input[0])
    
    user_input = [int(number) for number in user_input]
    
    temp_max1 = max(user_input)
    
    user_input.remove(temp_max1)
    
    temp_max2 = max(user_input)
    
    total = temp_max1 * temp_max2
    
    return print(total)

_ = input()
user_input = input().split(' ')
maxPairProduct(user_input)