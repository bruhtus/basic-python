challenge = 'thirty days of python'

#capitalize
print(f'capitalize: {challenge.capitalize()}')

#count
print(f"count y: {challenge.count('y')}")
print(f"count y from 7 to 10 (alphabet): {challenge.count('y', 7, 10)}") #count(substring, start, end)

#endswith()
print(f"using endswith (on): {challenge.endswith('on')}")

challenge_tabs = 'thirty\t days\t of\t python'

print(f'without expandtabs: {challenge_tabs}')
print(f'using expandtabs to replace tab (size=8) with spaces: {challenge_tabs.expandtabs()}')

print(f"find y: {challenge.find('y')}")
print(f"return highest index of y: {challenge.rfind('y')}")
print(f"return lowest index of y: {challenge.index('y')}")
print(f"return highest index of y: {challenge.rindex('y')}")

#check alphanumeric character
print(f'is challenge alphanumeric? {challenge.isalnum()}')

challenge_without_space = 'thritydaysofpython'
print(f'is challenge without space alphanumeric? {challenge_without_space.isalnum()}')

#check if alphabet character
print(f'is challenge alphabet character? {challenge.isalpha()}')

number = '123'
print(f'is number alphabet character? {number.isalpha()}')

#check if decimal (0-9) character
print(f'is challenge decimal character? {challenge.isdecimal()}')
print(f'is number decimal character? {number.isdecimal()}')

#check if character are numbers (0-9 and some unicode characters for numbers)
print(f'is challenge digit character? {challenge.isdigit()}')
print(f'is number digit character? {number.isdigit()}')
unicode_num = '\u00B2'
print(f'is unicode digit character? {unicode_num.isdigit()}')

#check if identifier
print(f'is challenge identifier? {challenge.isidentifier()}')
print(f'is challenge without space identifier? {challenge_without_space.isidentifier()}')

#strip
print(challenge.strip('noth'))

#split
print(challenge.split())

#return tittle cased string
print(challenge.title())
