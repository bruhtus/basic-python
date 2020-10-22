countries = [[('Finland', 'Helsinki')], [('sweden', 'stockholm')], [('norway', 'oslo')]]

lst = [{'country': members[0], 'city': members[1]} for row in countries for members in row]

print(lst)
