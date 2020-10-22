def cube(y):
    return y*y*y

g = lambda x: x*x*x
print(f'using lambda: {g(5)}')

print(f'using def: {cube(5)}')
