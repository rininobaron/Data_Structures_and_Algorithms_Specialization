user_input = input()

user_input = user_input.split(' ')

count = 0
total = 0
for number in user_input:
    total += int(number)
    count += 1
    # If the user input more than two numbers
    if count == 2:
        break
print(total)