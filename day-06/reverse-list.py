def reverse_list(*args):
    reverse = []
    #print(len(args[0]))
    #print(args[0][-2])
    print(type(args))
    for i in range(len(args[0])):
        reverse.append(args[0][-(i+1)])

    return reverse

print(reverse_list([1, 2, 3, 4, 5]))
