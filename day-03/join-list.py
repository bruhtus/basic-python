positive = [1, 2, 3]
zero = [0]
negative = [-3, -2, -1]

print(f'joining using extend() method: {negative.extend(positive)}') #can't using f-string for extend?
print(f'negative + zero + positive: {negative + zero + positive}')
negative.extend(zero)
negative.extend(positive)
print(f'joining using extend() method: {negative}')
