def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total += i
    return total

usr_input = input('Input a number: ')
int_input = int(usr_input)
print(f'sum of 0 to {int_input} is: {sum_of_numbers(int_input)}')
