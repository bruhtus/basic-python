def add_item(item, *added):
    item.append(added[0])
    print(type(added))

    return item

numbers = [1, 2, 3, 4]
print(add_item(numbers, 5))
