st1 = {'anu', 'ini', 'itu'}
st2 = {'anu', 'itu'}
st3 = {'ini', 'nganu'}
st4 = {'ngitu'}

print(f'is set 1 and set 2 disjoint? {st1.isdisjoint(st2)}')
print(f'is set 2 and set 1 disjoint? {st2.isdisjoint(st1)}\n') #the same

print(f'is set 1 and set 3 disjoint? {st1.isdisjoint(st3)}')
print(f'is set 1 and set 4 disjoint? {st1.isdisjoint(st4)}')
