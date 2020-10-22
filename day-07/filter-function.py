numbers = [1, 2, 3, 4, 5]

def is_even(num):
    if num % 2 == 0:
        return True

    return False

even_numbers = filter(is_even, numbers) #the filtering criteria is_even
print(list(even_numbers))
