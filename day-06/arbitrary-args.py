def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(sum_all_nums(2, 3, 5))

def generate_groups(team, *args):
    print(team)
    member = [i for i in args]
    return member

print(generate_groups('team-1', 'anu', 'ini', 'itu'))
