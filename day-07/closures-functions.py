def add_ten():
    ten = 10

    def add(num):
        return num + ten

    return add

closure_result = add_ten()
print(f'python closures functions: {closure_result(10)}')
